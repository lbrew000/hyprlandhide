import hyprland_interface as inter




def main():
    test_address = None
    all_clients = inter.get_clients()
    for client in all_clients:
        if(client['title'] == 'Steam'):
            test_address = client['address']
            print(client)
    test_cc = inter.get_window_by_class_and_title("Steam","steam")
    if(test_cc['address'] != test_address):
        print("Dammit")
    # inter.set_current_workspace(1)
    # print(get_active_workspace)
    # print(inter.get_active_workspace())

    # inter.focus_window(test_address)
    # print(inter.get_active_workspace())

    # print(active_w)   
main()