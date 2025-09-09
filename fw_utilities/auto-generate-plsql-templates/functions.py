import os
import sys

RIGA_VUOTA = "   "

out_parameter = []
out_temp_sql_head_code = []
out_temp_sql_body_code = []


def get_initial_parameters():
    risp = "NO"
    print("INSERIMENTO INIZIALE PARAMETRI")

    while (risp != "SI"):
        
        out_parameter.clear()

        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')

        nome_package = input("NOME DEL PACKAGE............: ").upper()
        owner = input("OWNER.......................: ").upper()
        other_schema = input("OTHER SCHEMA to EXECUTE on..: ").upper()
        risp = input("TUTTO CORRETTO? (SI/NO)...: ").upper()
        out_parameter.append(nome_package)
        out_parameter.append(owner)
        out_parameter.append(other_schema)
    return out_parameter


def crea_spec_code(inp_parametri):

    foutname = "outfiles/DDL_CREATE_PKG_"+inp_parametri[0].upper()+"_HEAD.sql"
    head_template = "pkg_TEMPLATE_head.sql"
    fout = open(foutname, "w+")
    finp_head_tmpl = open(head_template,"r")
    for line_head in finp_head_tmpl:
        out = str(line_head.replace('##OWNER##', inp_parametri[1], 1))
        out = out.replace('##PACKAGE_NAME##', inp_parametri[0], 1)
        out = out.replace('##OTHER_SCHEMAS##', inp_parametri[2], 1)
        out = out.replace('##SPOOL_NAME##', str("DDL_CREATE_PKG_" + inp_parametri[0].upper() + "_HEAD"), 1)
        #print(out)
        fout.write(out)
    finp_head_tmpl.close()
    fout.close()
    



def crea_body_code(inp_parametri):
    foutname = "outfiles/DDL_CREATE_PKG_"+inp_parametri[0].upper()+"_BODY.sql"
    body_template = "pkg_TEMPLATE_body.sql"
    fout = open(foutname, "w+")
    finp_body_tmpl=open(body_template,"r+")
    for line_body in finp_body_tmpl:
        out = str(line_body.replace('##OWNER##', inp_parametri[1], 1))
        out = out.replace('##PACKAGE_NAME##', inp_parametri[0], 1)
        out = out.replace('##OTHER_SCHEMAS##', inp_parametri[2], 1)
        out = out.replace('##SPOOL_NAME##', str(
            "DDL_CREATE_PKG_" + inp_parametri[0].upper() + "_BODY"), 1)

        #print(out)
        fout.write(out)

    finp_body_tmpl.close()
    fout.close()


