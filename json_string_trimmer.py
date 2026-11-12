import argparse,csv,json,sys
def transform(data):
    if isinstance(data,str): return data.strip()
    if isinstance(data,list): return [transform(x) for x in data]
    if isinstance(data,dict): return {k:transform(v) for k,v in data.items()}
    return data

def main():
    parser=argparse.ArgumentParser(description='JSON string trimmer')
    parser.add_argument("file",nargs="?",help="input path; defaults to stdin")
    args=parser.parse_args()
    source=open(args.file,encoding="utf-8",newline="").read() if args.file else sys.stdin.read()
    data=json.loads(source)
    result=transform(data)
    print(result if isinstance(result,str) else json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__": main()
