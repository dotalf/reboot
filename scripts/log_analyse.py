# encoding:utf-8

# kye = > (ip,url,code)
# value - > cnt

def loganalyse(logfile, topn=10):
    access_cnt = {}

    h1 = open(logfile, 'r')
    while True:
        ctx = h1.readline()
        # print ctx
        _log = ctx.split()
        if not ctx:
            break
        key = (_log[0], _log[6], _log[8])
        access_cnt[key] = access_cnt.get(key, 0) + 1
    h1.close()

    def sort_array(array):
        for i in range(0, len(array) - 1):
            for j in range(0, len(array) - 1 - i):
                if array[j][1] > array[j + 1][1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array

    result = sort_array(access_cnt.items())[-1:-topn - 1:-1]
    # print result

    # h2 = open('result.txt', 'w+')

    # for i in range(0, len(result) - 1):
    #     node = result[i]
    #     type(node)
    #     #	print node[1], node[0][0],node[0][1],node[0][2]
    #     h2.write('%s %s %s %s\n' % (node[1], node[0][0], node[0][1], node[0][2]))

    # h2.close()

    h3 = open('top10.tpl', 'r+')
    page = h3.read()
    h3.close()

    title = 'TOP %s访问日志' % topn
    thead = '\n<th>IP</th>\n<th>URL</th>\n<th>CODE</th>\n<th>CNT</th>'
    tbody = ''
    for node in result:
        tbody += '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>\n' % (
            node[0][0], node[0][1], node[0][2], node[1])
    return page.format(title=title, thead=thead, tbody=tbody)

    # h4 = open(despath, 'w+')
    # h4.write(page.format(title=title, thead=thead, tbody=tbody))
    # h4.close()


if __name__ == '__main__':
    logfile = 'ngnix.log'
    despath = 'top10.html'
    despath5 = 'top5.html'
    despath8 = 'top8.html'
    loganalyse(logfile, despath)
    loganalyse(logfile, despath5, 5)
    loganalyse(logfile, despath8, 8)
