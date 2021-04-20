import rouge

def compute_rouge(src_file,tgt_files:list,file):
    with open(file,'w') as out:
        for aggregator in ['Avg', 'Best', 'Individual']:
            out.write('Evaluation with {} \n'.format(aggregator))
            apply_avg = aggregator == 'Avg'
            apply_best = aggregator == 'Best'

            evaluator = rouge.Rouge(metrics=['rouge-n', 'rouge-l', 'rouge-w'],
                                   max_n=4,
                                   limit_length=True,
                                   length_limit=100,
                                   length_limit_type='words',
                                   apply_avg=apply_avg,
                                   apply_best=apply_best,
                                   alpha=0.5, # Default F1_score
                                   weight_factor=1.2,
                                   stemming=True)

            output = []
            tgt = []

            with open(src_file, "r") as f:
                output = [i.lower().replace('<unk>', '').replace('#','').replace('_','') for i in f.readlines()]

            for i in tgt_files:
                with open(i, "r") as f:
                    tgt.append([i.lower().replace('#','').replace('_','') for i in f.readlines()])

            num_ref = len(tgt_files)
            all_references = []
            for i in range(len(output)):
                temp_refs=[]
                for j in range(num_ref):
                    temp_refs.append(tgt[j][i])
                all_references.append(temp_refs)

            all_hypothesis = output


            scores = evaluator.get_scores(all_hypothesis, all_references)

            def prepare_results(p, r, f):
                return '\t{}:\t{}: {:5.2f}\t{}: {:5.2f}\t{}: {:5.2f}'.format(metric, 'P', 100.0 * p, 'R', 100.0 * r,
                                                                             'F1', 100.0 * f)

            for metric, results in sorted(scores.items(), key=lambda x: x[0]):
                if not apply_avg and not apply_best: # value is a type of list as we evaluate each summary vs each reference
                    for hypothesis_id, results_per_ref in enumerate(results):
                        nb_references = len(results_per_ref['p'])
                        for reference_id in range(nb_references):
                            out.write('\tHypothesis #{} & Reference #{}: \n'.format(hypothesis_id, reference_id))
                            out.write('\t' + prepare_results(results_per_ref['p'][reference_id], results_per_ref['r'][reference_id], results_per_ref['f'][reference_id])+'\n')
                    out.write('\n')
                else:
                    out.write(prepare_results(results['p'], results['r'], results['f'])+'\n')
            out.write('\n')



if __name__ == '__main__':
    #compute_rouge("/Users/leo/Desktop/桌面/NLPDataset/xsum_raw/lead3-n.txt","/Users/leo/Desktop/桌面/NLPDataset/xsum_raw/lead3-n.txt.tgt","lead3_xsum_rouges.txt")
    compute_rouge("/Users/leo/Desktop/桌面/NLPDataset/samsum_raw/test_text_rank.txt",["/Users/leo/Desktop/桌面/NLPDataset/samsum_raw/lead3-n.txt.tgt"],"textrank3_samsum_rouges.txt")
    #compute_rouge("/Users/leo/Desktop/桌面/NLPDataset/cnndm/lead3-n.txt","/Users/leo/Desktop/桌面/NLPDataset/cnndm/lead3-n.txt.tgt","lead3_cnndm_rouges.txt")
    #compute_rouge("/Users/leo/Desktop/桌面/NLPDataset/ricos/lead3-n.txt",["/Users/leo/Desktop/桌面/NLPDataset/ricos/last3-n.txt.tgt1","/Users/leo/Desktop/桌面/NLPDataset/ricos/last3-n.txt.tgt2","/Users/leo/Desktop/桌面/NLPDataset/ricos/last3-n.txt.tgt3"],"lead3_ricos_rouges.txt")
    # compute_rouge("/Users/leo/Desktop/桌面/NLPDataset/ricos/mid3-n.txt",
    #               ["/Users/leo/Desktop/桌面/NLPDataset/ricos/last3-n.txt.tgt1",
    #                "/Users/leo/Desktop/桌面/NLPDataset/ricos/last3-n.txt.tgt2",
    #                "/Users/leo/Desktop/桌面/NLPDataset/ricos/last3-n.txt.tgt3"], "mid3_ricos_rouges.txt")
    # compute_rouge("/Users/leo/Desktop/桌面/NLPDataset/ricos/last3-n.txt",
    #               ["/Users/leo/Desktop/桌面/NLPDataset/ricos/last3-n.txt.tgt1",
    #                "/Users/leo/Desktop/桌面/NLPDataset/ricos/last3-n.txt.tgt2",
    #                "/Users/leo/Desktop/桌面/NLPDataset/ricos/last3-n.txt.tgt3"], "last3_ricos_rouges.txt")
    compute_rouge("/Users/leo/Desktop/桌面/NLPDataset/ricos/test_text_rank.txt",
                  ["/Users/leo/Desktop/桌面/NLPDataset/ricos/last3-n.txt.tgt1",
                   "/Users/leo/Desktop/桌面/NLPDataset/ricos/last3-n.txt.tgt2",
                   "/Users/leo/Desktop/桌面/NLPDataset/ricos/last3-n.txt.tgt3"], "textrank3_ricos_rouges.txt")
