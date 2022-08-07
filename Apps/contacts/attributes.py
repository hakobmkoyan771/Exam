#!/usr/bin/python3

def generatorHtml(user_list):
    head = """<!DOCTYPE html>
            <html>
            <head>
                <style>
                    table {
                        border-collapse: collapse;
                        width: 100%;
                        }

                    th, td {
                        text-align: left;
                        padding: 8px;
                    }

                    tr:nth-child(even) {
                        background-color: #CFFFCE;
                    }
                    
                    tr:nth-child(odd) {
                        background-color: #A8FFA7;
                    }
                    
                    .registerbtn {
                        background-color: #04AA6D;
                        color: white;
                        padding: 16px 20px;
                        margin: 8px 0;
                        border: none;
                        cursor: pointer;
                        width: 10%;
                        opacity: 0.9;
                    }

                    .registerbtn:hover {
                        opacity: 1;
                    }
                </style>
                <title>Users List</title>
            </head>"""

    body = """<body>
              <table background-color: #04AA6D>
                  <tr>
                    <td>Mail</td>
                    <td>Name</td>
                    <td>Surname</td>
                  </tr>"""
    for i in range(0, len(user_list), 3):
        body += """<tr>"""
        body += """<td>""" + str(user_list[i]) + """</td>"""
        body += """<td>""" + str(user_list[i+1]) + """</td>"""
        body += """<td>""" + str(user_list[i+2]) + """</td>"""

    body += """</table>
                </body>
                </html>"""

    indexfile = head + body
    return indexfile
#    with open("templates/contacts.html", "w") as htmlfile:
#        htmlfile.write(indexfile)


def users_on_html(users_list):
    ulist = []
    for i in users_list:
        for k, v in i.items():
            if k != "_id":
                ulist.append(v)
    return generatorHtml(ulist)
