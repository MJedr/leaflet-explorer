import subprocess


def get_database_info(host, user):
    records, _ = subprocess.Popen(['psql','-lA','-F\x02','-R\x01','-h',host,'-U',user ],stdout=subprocess.PIPE).communicate()
    records = records.split('\x01')
    header = records[1].split('\x02')
    return [dict(zip(header,line.split('\x02'))) for line in records[2:-1]]

print(get_database_info(b'marcysia',b'marcysia'))