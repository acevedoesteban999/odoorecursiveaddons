import sys
import os
import configparser


def expand_addons_path_recursive_from_config():
    
    config_file = None
    for i, arg in enumerate(sys.argv):
        if arg == '-c' and i + 1 < len(sys.argv):
            config_file = sys.argv[i + 1]
            break
        elif arg.startswith('--config='):
            config_file = arg.split('=', 1)[1]
            break
    
    if not config_file or not os.path.exists(config_file):
        return None
    
    cp = configparser.ConfigParser()
    cp.read(config_file)
    
    if not cp.has_option('options', 'addons_path_recursive'):
        return None
    
    original_path = cp.get('options', 'addons_path_recursive')
    paths = []

    def _is_valid_module_name(name):
        if not name:
            return False
        if name.startswith('.') or name.startswith('_'):
            return False
        if name.startswith('-'):
            return False
        if ' ' in name:
            return False
        return True

    def _has_modules_inside(_path):
        for sub in os.listdir(_path):
            if not _is_valid_module_name(sub):
                continue
            sub_path = os.path.join(_path, sub)
            if not os.path.isdir(sub_path):
                continue
            if os.path.exists(os.path.join(sub_path, '__manifest__.py')) or \
               os.path.exists(os.path.join(sub_path, '__openerp__.py')):
                return True
            if _has_modules_inside(sub_path):
                return True
        return False

    def _proccess_path_recursive(path):
        try:
            if not os.path.isdir(path):
                return
            
            for _sub_path in os.listdir(path):
                
                if not _is_valid_module_name(_sub_path):
                    continue
                
                sub_path = os.path.join(path, _sub_path)
                if not os.path.isdir(sub_path):
                    continue
                
                
                if path not in paths and os.path.exists(os.path.join(sub_path, '__manifest__.py')):
                    paths.append(path)
                elif not os.path.exists(os.path.join(sub_path, '__manifest__.py')):
                   _proccess_path_recursive(sub_path) 


        except:
            pass

    for path in original_path.split(','):
        path = path.strip()
        _proccess_path_recursive(path)


    return paths
