```python
# This code has been designed to test the Seq class via pytest
# Seq object Class
class Seq:
    def __init__(self,DNAsequence):
        self.sequence = DNAsequence
        
    def count_kmers(self,k,counter={}):
        counter={}
        assert len(self.sequence) > 0
        for i in self.sequence:
            assert i == 'A' or i == 'T' or i == 'C' or i == 'G'
        if len(self.sequence) >= k > 0 and isinstance(k,int) == True:
            if k > 1:
                for i,base in enumerate(self.sequence[:-k+1]):
                    kmer = self.sequence[i:i+k]
                    if kmer in counter:
                        counter[kmer]+=1
                    else:
                        counter[kmer]=1
            else:
                for i in self.sequence:
                    if i in counter:
                        counter[i]+=1
                    else:
                        counter[i]=1
            return(counter)
        else:
            print('Invalid kmer entry. Returning empty counter')
            return(counter)
    
    def get_pandas(self,n=4):
        panda_frame = pd.DataFrame(columns=['k','Observed kmers','Possible kmers'])
        k=0
        L=0
        assert len(self.sequence) > 0
        assert isinstance(n,int)
        assert n > 0
        for i in self.sequence:
            assert i == 'A' or i == 'T' or i == 'C' or i == 'G'
        for i in self.sequence:
            L+=1
        for i in self.sequence:
            k+=1
            observed_kmers=0
            counter={}
            if k > 1:
                for i,base in enumerate(self.sequence[:-k+1]):
                    kmer = self.sequence[i:i+k]
                    if kmer in counter:
                        counter[kmer]+=1
                    else:
                        counter[kmer]=1
            else:
                for i in self.sequence:
                    if i in counter:
                        counter[i]+=1
                    else:
                        counter[i]=1
            for i in counter:
                observed_kmers+=1
            if L < (n**k):
                possible_kmers=L-k+1
            else:
                possible_kmers=n**k
            panda_frame.loc[k] = [k,observed_kmers,possible_kmers]
        total_observed = panda_frame['Observed kmers'].sum()
        total_possible = panda_frame['Possible kmers'].sum()
        panda_frame.loc[k+1] = ['Total',total_observed,total_possible]
        return panda_frame
    
    def graph_pandas(self,data_frame):
        assert set(['k','Observed kmers','Possible kmers']).issubset(data_frame)
        data_frame['Proportion'] = data_frame['Observed kmers'] / data_frame['Possible kmers']
        graph_frame = data_frame[['k','Proportion']]
        graph_frame.plot(kind='bar',title="Proportion of Observed vs Actual kmers");
    
    def ling_comp(self,data_frame):
        assert set(['k','Observed kmers','Possible kmers']).issubset(data_frame)
        observed_total = data_frame.iloc[-1,1]
        observed_possible = data_frame.iloc[-1,2]
        linguistic_complexity = observed_total/observed_possible
        return linguistic_complexity

# Test code
def test_count_kmers_2():
    testobj = Seq('ATTTGGATT').count_kmers(2)
    assert len(testobj) == 5
    print("PASS")
def test_count_kmers_0():
    testobj = Seq('ATTTGGATT').count_kmers(0)
    assert len(testobj) == 0
    print("PASS")
def test_count_kmers_1k():
    testobj = Seq('ATTTGGATT').count_kmers(1000)
    assert len(testobj) == 0
    print("PASS")
def test_count_kmers_neg():
    testobj = Seq('ATTTGGATT').count_kmers(-2)
    assert len(testobj) == 0
    print("PASS")
def test_count_kmers_dec():
    testobj = Seq('ATTTGGATT').count_kmers(0.2)
    assert len(testobj) == 0
    print("PASS")
def test_count_kmers_not_empty():
    testobj = len(Seq('ATTTGGATT').count_kmers(2))
    assert testobj > 0
    print('PASS')
def test_get_pandas_input():
    testobj = Seq('ATTTGGATT').sequence
    testobj_len = len(testobj)
    assert testobj_len > 0
    print('PASS')
def test_get_pandas_output():
    testpandas = Seq('ATTGGATT').get_pandas()
    assert set(['k','Observed kmers','Possible kmers']).issubset(testpandas)
    print('PASS')
def test_graph_pandas_input(): # Tests the pandas frame that goes into graph_pandas
    testpandas = Seq('ATTTGGATT').get_pandas()
    assert type(testpandas) == pd.core.frame.DataFrame # Asserts that the input is a pandas frame
    assert set(['k','Observed kmers','Possible kmers']).issubset(testpandas) # Asserts that the pandas was created by get_pandas
    print('PASS')
def test_ling_comp_input():
    testpandas = Seq('ATTTGGATT').get_pandas()
    assert type(testpandas) == pd.core.frame.DataFrame # Asserts that the input is a pandas frame
    assert set(['k','Observed kmers','Possible kmers']).issubset(testpandas) # Asserts that the pandas was created by get_pandas
    observed_total = testpandas.iloc[-1,1]
    assert isinstance(observed_total,int) 
    observed_possible = testpandas.iloc[-1,2]
    assert isinstance(observed_possible,int)
    assert observed_total > 0
    assert observed_possible > 0
    print('PASS')
def test_ling_comp_output():
    testpandas = Seq('ATTTGGATT').get_pandas()
    testlingcomp = Seq('ATTTGGATT').ling_comp(testpandas)
    assert isinstance(testlingcomp,int) or isinstance(testlingcomp,float)
    assert(testlingcomp>0)
    print('PASS')
