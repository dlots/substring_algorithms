# Лабораторная работа №1: Поиск подстроки в строке
### 18ПМИ Богородицкая Екатерина, Сазанов Дмитрий, Селивановская Дарья


```python
from knuth_morris_pratt import knuth_morris_pratt as kmp
from naive import naive
from aho_corasick import aho_corasick as ac
from boyer_moore_horspool import boyer_moore_horspool as bmh
from rabin_karp import rabin_karp as rk
```


```python
bad_w = []
bad_t = []
good_w = []
good_t = []
for i in range(1,5):
    f = open('benchmarks/bad_w_' + str(i) + '.txt', encoding='utf-8')
    bad_w.append(f.read())
    f.close()
    f = open('benchmarks/bad_t_' + str(i) + '.txt', encoding='utf-8')
    bad_t.append(f.read())
    f.close()
    f = open('benchmarks/good_w_' + str(i) + '.txt', encoding='utf-8')
    good_w.append(f.read())
    f.close()
    f = open('benchmarks/good_t_' + str(i) + '.txt', encoding='utf-8')
    good_t.append(f.read())
    f.close()
#print(bad_w)
#print(bad_t)
#print(good_w)
#print(good_t)
```


```python
algorithms = [kmp, naive, ac, bmh, rk]
#algorithms = [ac]
```

<h3>Время работы</h3>


```python
import time


def check_time(f, *args):
    start = time.time()
    f(*args)
    return time.time() - start
```


```python
mas_text = bad_t + good_t
mas_pat = bad_w + good_w
```


```python
for a in algorithms:
    print(a.__name__)
    mas_time = []
    temp = 0.
    for i in range(8):
        temp = 0.
        #print(mas_text[i])
        if a.__name__ == 'aho_corasick':
            pat = [mas_pat[i]]
        else:
            pat = mas_pat[i]
        #print(ord(mas_text[i][0]))
        for j in range(10):
            temp += check_time(a, mas_text[i], pat)
        print("Test", i+1, "время работы = ", temp/10)
    print('')
```

    knuth_morris_pratt
    Test 1 время работы =  0.00010285377502441406
    Test 2 время работы =  0.00011663436889648437
    Test 3 время работы =  0.0012163162231445313
    Test 4 время работы =  0.008805203437805175
    Test 5 время работы =  0.0010000228881835937
    Test 6 время работы =  0.0014239311218261718
    Test 7 время работы =  0.004204964637756348
    Test 8 время работы =  0.013412117958068848
    
    naive
    Test 1 время работы =  0.0
    Test 2 время работы =  0.0011039972305297852
    Test 3 время работы =  0.08047342300415039
    Test 4 время работы =  4.350687766075135
    Test 5 время работы =  0.0009054899215698242
    Test 6 время работы =  0.0015000343322753907
    Test 7 время работы =  0.0044448614120483395
    Test 8 время работы =  0.012900972366333007
    
    aho_corasick
    Test 1 время работы =  0.00010395050048828125
    Test 2 время работы =  0.0006964206695556641
    Test 3 время работы =  0.01301436424255371
    Test 4 время работы =  0.8062058210372924
    Test 5 время работы =  0.002101492881774902
    Test 6 время работы =  0.010702991485595703
    Test 7 время работы =  0.1600804805755615
    Test 8 время работы =  0.02970287799835205
    
    boyer_moore_horspool
    Test 1 время работы =  0.0
    Test 2 время работы =  0.00019855499267578124
    Test 3 время работы =  0.0020134449005126953
    Test 4 время работы =  0.008604860305786133
    Test 5 время работы =  0.00020000934600830078
    Test 6 время работы =  9.999275207519531e-05
    Test 7 время работы =  0.0007999897003173828
    Test 8 время работы =  0.0011963844299316406
    
    rabin_karp
    Test 1 время работы =  0.0
    Test 2 время работы =  0.00010328292846679687
    Test 3 время работы =  0.0018009662628173829
    Test 4 время работы =  0.007695293426513672
    Test 5 время работы =  0.0011571884155273438
    Test 6 время работы =  0.0020011425018310546
    Test 7 время работы =  0.007797813415527344
    Test 8 время работы =  0.01871984004974365
    
    

<h3>Количество сравнений</h3>


```python
for a in algorithms:
    print(a.__name__)
    for i in range(8):
        if a.__name__ == 'aho_corasick':
            pat = [mas_pat[i]]
        else:
            pat = mas_pat[i]
        #print(pat)
        ans, comp = a(mas_text[i], pat)
        print("Test", i+1, "количество сравнений = ", comp, ", позиции = ", ans)
    print('')
```

    knuth_morris_pratt
    Test 1 количество сравнений =  18 , позиции =  [8]
    Test 2 количество сравнений =  190 , позиции =  [90]
    Test 3 количество сравнений =  1900 , позиции =  [900]
    Test 4 количество сравнений =  9000 , позиции =  [4000]
    Test 5 количество сравнений =  697 , позиции =  [599]
    Test 6 количество сравнений =  1074 , позиции =  [610]
    Test 7 количество сравнений =  3150 , позиции =  [1629]
    Test 8 количество сравнений =  10623 , позиции =  [9522]
    
    naive
    Test 1 количество сравнений =  19 , позиции =  [8]
    Test 2 количество сравнений =  955 , позиции =  [90]
    Test 3 количество сравнений =  95050 , позиции =  [900]
    Test 4 количество сравнений =  4500500 , позиции =  [4000]
    Test 5 количество сравнений =  714 , позиции =  [599]
    Test 6 количество сравнений =  1158 , позиции =  [610]
    Test 7 количество сравнений =  3554 , позиции =  [1629]
    Test 8 количество сравнений =  10714 , позиции =  [9522]
    
    aho_corasick
    Test 1 количество сравнений =  18 , позиции =  {'ab': [8]}
    Test 2 количество сравнений =  190 , позиции =  {'aaaaaaaaab': [90]}
    Test 3 количество сравнений =  1900 , позиции =  {'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab': [900]}
    Test 4 количество сравнений =  9000 , позиции =  {'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab': [4000]}
    Test 5 количество сравнений =  714 , позиции =  {'сын князя Василия': [599]}
    Test 6 количество сравнений =  1159 , позиции =  {'Да, я слышал про его план вечного мира, и это очень интересно, но едва ли возможно...': [610]}
    Test 7 количество сравнений =  3540 , позиции =  {'вспоминал свое обещание, но тут же, как это бывает с людьми, называемыми бесхарактерными, ему так страстно захотелось войти взглянуть еще раз на эту столь знакомую и надоевшую ему беспутную жизнь, и невольно пришла в голову мысль, что данное слово ничего не значит, к тому же, еще прежде, чем князю Андрею, он дал также Анатолю слово привезти долг; наконец, он подумал, что все эти': [1629]}
    Test 8 количество сравнений =  10715 , позиции =  {'Бутылка рому была принесена; раму, не пускавшую сесть на наружный откос окна, выламывали два': [9522]}
    
    boyer_moore_horspool
    Test 1 количество сравнений =  31 , позиции =  [8]
    Test 2 количество сравнений =  293 , позиции =  [90]
    Test 3 количество сравнений =  2903 , позиции =  [900]
    Test 4 количество сравнений =  14003 , позиции =  [4000]
    Test 5 количество сравнений =  231 , позиции =  [599]
    Test 6 количество сравнений =  283 , позиции =  [610]
    Test 7 количество сравнений =  987 , позиции =  [1629]
    Test 8 количество сравнений =  1520 , позиции =  [9522]
    
    rabin_karp
    Test 1 количество сравнений =  29 , позиции =  [8]
    Test 2 количество сравнений =  283 , позиции =  [90]
    Test 3 количество сравнений =  2803 , позиции =  [900]
    Test 4 количество сравнений =  13003 , позиции =  [4000]
    Test 5 количество сравнений =  2053 , позиции =  [599]
    Test 6 количество сравнений =  3325 , позиции =  [610]
    Test 7 количество сравнений =  9607 , позиции =  [1629]
    Test 8 количество сравнений =  32193 , позиции =  [9522]
    
    


```python

```
