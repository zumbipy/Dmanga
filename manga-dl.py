import os
from source import VERSAO


print(
    f"""
+-----------------------------------------------------------+                     
|     __  __         Manga Download.               _   _    |                     
|    |  \/  |  __ _   _ _    __ _   __ _   ___   __| | | |  |                    
|    | |\/| | / _` | | ' \  / _` | / _` | |___| / _` | | |  |                   
|    |_|  |_| \__,_| |_||_| \__, | \__,_|       \__,_| |_|  |                 
|                            |___/         {VERSAO}            |  
+-----------------------------------------------------------+  
Pasta Atual: {os.path.basename(os.path.abspath(''))}
"""
)
