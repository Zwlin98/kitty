# https://sw.kovidgoyal.net/kitty/remote-control/#customizing-authorization-with-your-own-program
def is_cmd_allowed(pcmd, window, from_socket, extra_data):
    cmd_name = pcmd['cmd']
    allowed_cmds = ['set-tab-title']
    return cmd_name in allowed_cmds

