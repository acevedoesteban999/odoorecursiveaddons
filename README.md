# OdooRecursiveAddons

Expand `addons_path` recursively from the Odoo configuration file.

## Installation

```bash
pip install odoorecursiveaddons

### Use 
    from odoorecursiveaddons import expand_addons_path_recursive_from_config

    paths = expand_addons_path_recursive_from_config()
    print(paths)  
```



## Use odoo.conf
[options]
addons_path_recursive = /route/to/addons


The function searches for directories containing Odoo modules recursively.


