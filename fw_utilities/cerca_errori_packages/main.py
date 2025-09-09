from  funzioni import *




if __name__ == "__main__":
    ambiente = input("Inserisci l'ambiente (DEV1, DEV2, DEV3, INT1, INT2): ").strip()
    package_name = input("Inserisci il nome del package: ").strip()
    if ambiente == "":
        get_dba_errors('DEV2',package_name)
    else:
        get_dba_errors(ambiente, package_name)
