import textwrap

def wrap(string, max_width):
    wrapped = textwrap.wrap(string, max_width)
    final_str = ""
    for w in wrapped:
        final_str += w + '\n'
        
    
    return final_str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)