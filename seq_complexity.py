```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
%matplotlib inline

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
        #for i in self.sequence:
            #assert i == 'A' or i == 'T' or i == 'C' or i == 'G'
        for i in self.sequence: # FIX
            if not i == 'A' or i == 'T' or i == 'C' or i == 'G':
                if i in errorcount:
                    errorcount[i]+=1
                else:
                    errorcount[i]=1 #FIX
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
        
if __name__ = '__main__':
	for filename in glob.glob('*fasta'):
    f = open(filename,'r')
    fasta = f.readlines()
    for line_number,line in enumerate(fasta):
        line = line.rstrip()
        if line_number%3 == 0:
            seq_line_num = line_number + 1
            for line_number,line in enumerate(fasta):
                if line_number == seq_line_num:
                    seq_string = str(line)
                    seq_obj = Seq(seq_string)
                    seq_obj_pandas = seq_obj.get_pandas()
                    seq_obj_graph = seq_obj.graph_pandas(seq_obj_pandas)
                    seq_obj_lingcomp = seq_obj.ling_comp(seq_obj_pandas)
                    ssol = str(seq_obj_lingcomp)
                        return seq_obj_pandas
                        return seq_obj_graph
                    print(ssol)

```
I had attempted to code the main function so that it would create a directory for each DNA sequence, and store in it a pandas table (as .csv file), graph (as a .png file), and a .txt file (containg the value of the linguistic complexity as a string). Unfortunatly, I was unable to complete this version of the function; my unfinished function is as follows:

```python
if __name__ = '__main__':
    for filename in glob.glob('*fasta'):
    f = open(filename,'r')
    fasta = f.readlines()
    for line_number,line in enumerate(fasta):
        line = line.rstrip()
        if line_number%3 == 0:
            dirpath = os.path.join('./', line[1:])
            try:
                os.mkdir(dirpath)
            except FileExistsError:
                print('Directory {} already exists'.format(dirpath))
            else:
                print('Directory {} created'.format(dirpath))
            seq_line_num = line_number + 1
            for line_number,line in enumerate(fasta):
                if line_number == seq_line_num:
                    seq_string = str(line)
                    seq_obj = Seq(seq_string)
                    seq_obj_pandas = seq_obj.get_pandas()
                    seq_obj_graph = seq_obj.graph_pandas(seq_obj_pandas)
                    seq_obj_lingcomp = seq_obj.ling_comp(seq_obj_pandas)
                    newFile_pandas = dirpath +'/Seq_pandas.csv'
                    if not os.path.exists(os.path.dirname(newFile_pandas)):
                        os.makedirs(os.path.dirname(newFile_pandas))
                    newFile_graph = dirpath + '/Seq_graph.png'
                    if not os.path.exists(os.path.dirname(newFile_graph)):
                        os.makedirs(os.path.dirname(newFile_graph))
                    newFile_lingcomp = dirpath + '/Seq_lingcomp.txt'
                    if not os.path.exists(os.path.dirname(newFile_lingcomp)):
                        os.makedirs(os.path.dirname(newFile_lingcomp))
                    seq_obj_pandas.to_csv(newFile_pandas)
                    seq_obj_graph.figure.savefig(newFile_graph)
                    with open(newFile, 'a') as foo:
                        foo.write('\nLinguistic Composition')
                        ssol = str(seq_obj_lingcomp)
                        foo.write(ssol)
```
