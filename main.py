from xml.sax.handler import property_dom_node
from metodo import Metodo

if __name__ == '__main__':
    proyecto = Metodo()
    proyecto.print_info()
    proyecto.carga_val()
    proyecto.show_values()
    proyecto.show_cloud()
    proyecto.calc_poli()
    proyecto.show_matrix()
    proyecto.show_func()
    proyecto.show_both()
