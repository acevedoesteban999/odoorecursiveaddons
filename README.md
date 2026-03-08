# OdooRecursiveAddons

This module enables recursive addon loading for odoo-bin, making it ideal for developers managing multiple projects, repositories, and modules across various directories. Instead of manually adding every path to the .conf file, developers can use a single recursive configuration option that automatically discovers all valid Odoo modules within nested folder structures.

Expand `addons_path` recursively from the Odoo configuration file.

## Installation
```
    pip install odoorecursiveaddons
```
## Use in odoo-bin
```
    from odoorecursiveaddons import expand_addons_path_recursive_from_config

    if __name__ == "__main__":
        for path in expand_addons_path_recursive_from_config():
            if path not in odoo.addons.__path__:
                odoo.addons.__path__.append(path)
        odoo.cli.main()
    
```

## Use in odoo.conf
```
    [options]
    addons_path_recursive = /route/to/addons
```


