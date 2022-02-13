# CS238 Programming Assignment
## Progress
1. Finished the basic algorithmic version
2. Need to implement backtracing
3. Need to implement DC approach and O(n) space
## Prompt
We will discuss a space-saving technique for pairwise sequence alignment
    based on divide-and-conquer this week. The technique can be easily
    extended to multiple sequence alignment. Your task is to design an
    O(m*n) space, O(m*n*k) time SP alignment algorithm for three DNA
    sequences of lengths m, n and k, respectively. Implement your algorithm
    in C/C++/Java/Python, and test it on real data.

You may find discussions on the space-saving technique for pairwise 
    sequence comparison in the books by Jones and Pevzner, by Gusfield, 
    and by Jiang, Xu, and Zhang (Current Topics in Computational Biology, 
    MIT Press Series on Computational Molecular Biology, 2002). The 
    following original papers provide more detailed information:

    D.S. Hirschberg. Algorithms for the longest common subsequence
    problem. J.ACM, 24:664-75, 1977.

    E. W. Myers and W. Miller. Optimal alignments in linear space.
    Comp. Appl. Biosciences, 4:11-17, 1988.
    At UCR Science Lib: call number is QH324.2 .C66 

    Chao, Hardison, and Miller. Recent developments in linear-space
    alignment methods: a survey. Journal of Computational Biology.
    Vol. 1-4, pp. 271-291. 1994. 

1. For simplicity, let's consider global alignment and the basic 
         SP score model where gaps are not specially treated. 

2. Your program should work for any score function on nucleotides.
         In other words, the user should be able to input a score function in the form of a 
5x5 matrix indexed by A, C, G, T, and space. The SP-score of a column of letters/spaces is the sum of the 
scores of each pair of letters/spaces in the column.

3. To test your program, use the Blast scores: Match = 5, Mismatch = -4,
     and Indel = -8. The score between two spaces is 0.
## Testing
Test your program on the following five sets of sequences:
1. **NM_013096**.  Rattus norvegicus hemoglobin alpha, adult chain 2 (Hba-a2),
                     mRNA. 557 bps.
         **NM_008218**.  Mus musculus hemoglobin alpha, adult chain 1 (Hba-a1), 
                     mRNA. 569 bps.
         **NM_000558**.  Homo sapiens hemoglobin, alpha 1 (HBA1), mRNA. 577 bps.

2. **NM_001030004**. Homo sapiens hepatocyte nuclear factor 4, alpha 
                       (HNF4A), transcript variant 6, mRNA. 1558 bps.
**NM_178850**.    Homo sapiens hepatocyte nuclear factor 4, alpha 
                       (HNF4A), transcript variant 3, mRNA. 1652 bps.
         **NM_001287184**. Homo sapiens hepatocyte nuclear factor 4 alpha (HNF4A), 
                       transcript variant 10, mRNA. 1780 bps.

3. **NM_010019**. Mus musculus death-associated protein kinase 2 (Dapk2),
                    mRNA, 1792 bps.
         **NM_001243563**. Sus scrofa death-associated protein kinase 2 (DAPK2),
                    mRNA, 1825 bps.
         **NM_014326**. Homo sapiens death-associated protein kinase 2 (DAPK2), 
                    mRNA, 2791 bps.

4. **NM_008261**. Mus musculus hepatic nuclear factor 4 (Hnf4). 4391 bps
         **NM_000457**. Homo sapiens hepatocyte nuclear factor 4, alpha (HNF4A), 
                    transcript variant 2, mRNA. 4739 bps
         **XM_016937951**. PREDICTED: Pan troglodytes hepatocyte nuclear factor 4 
                    alpha (HNF4A), transcript variant X1, mRNA, 4724 bps

5. **NM_000492**. Homo sapiens cystic fibrosis transmembrane conductance
                    regulator (ATP-binding cassette sub-family C, member 7) 
                    (CFTR), mRNA. 6070 bps
         **NM_021050**. Mus musculus cystic fibrosis transmembrane conductance
                    regulator homolog (Cftr), mRNA. 6305 bps.
         **NM_031506**. Rattus norvegicus cystic fibrosis transmembrane 
                    conductance regulator homolog (Cftr), mRNA. 6287 bps.

You may retrieve the sequences at http://www.ncbi.nih.gov/
using the accession numbers NM_013096, etc.  Select "nucleotide" in 
         the search option box. The sequence data is given at the bottom of 
         the search result page. Note that the last dataset may take your 
         algorithms quite some time to run, especially on an old computer.
## Report
For this question, submit a report (hard copy) along with HW3 with
                                                  
1. a high-level description of your algorithm (i.e. high-level
        pseudo-code), and the data structures used,
2. your source code, and
3. the result of your program on each dataset, including the
    score of the optimal alignment obtained, the length of the alignment,
   the number of columns with perfectly matched nucleotides in the
   alignment, and the running time and memory (on a PC or laptop
   with specification of CPU and memory). Please do not include
   the actual alignment in the report (because it is going to be quite
   loooong :-). p
4. Do you see any obvious conserved regions captured in your alignments?


   Although this question is optional for HW2, it could be a very good idea
   that you complete the dynamic programming routine for computing the 
   optimal score of a 3-sequence alignment in O(m*n) space, and test it on
   some small data to make sure that it is correct. The recurrence relation is
   given in Chapter 6.10 of the textbook. Note that this algorithm will need
   the dynamic programming algorithm for pairwise sequence alignment to 
   initialize its matrix.


   Also, although your goal is to implement the O(mn)-space algorithm, it
   will be useful for you to implement the standard O(mnk)-space dynamic 
   programming algorithm for 3-sequence alignment and use it as a subroutine 
   in the divide-and-conquer process when one of the sequences degenerates 
   to one or zero letters.
