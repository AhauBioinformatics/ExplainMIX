<div align="center">
  <img src="https://github.com/Xiang010Ying/Drug-response-ExplainMIX/blob/main/picture/explainMIX_logo.png" alt="avatar"> 
</div>
<center> &#8195 &#8195 &#8195 Explaining Drug Response Prediction in Directed Graph Neural Networks with Multi-Omics Fusion. </center>

<br/><br/>

# Drug-response-ExplainMIX
## Why we start this research?
In the field of drug response prediction, substantial progress has been made, driven by cutting-edge technologies like deep learning. These advancements have resulted in remarkably accurate predictions, raising hopes for more effective treatments. However, the translation of these promising models from research to clinical practice faces significant hurdles. One of the most formidable challenges is the inherent "black-box" nature of these advanced algorithms.

Clinicians and researchers are confronted with the predicament of relying on predictions without comprehending the rationale behind them. In the context of healthcare, especially in critical decisions involving patient well-being, having insight into why a particular prediction is made is paramount. Without this transparency, the adoption of predictive models in clinical settings remains limited.
## Overview of our research content
This paper introduces ExplainMIX, a approach that fuses multi-omics data within heterogeneous graph neural networks to tackle the fundamental challenges of drug response prediction. ExplainMIX adeptly captures intricate structures and nuanced semantics within heterogeneous graphs, enhancing both predictive and interpretive capabilities. By leveraging node-level information and logical semantics for edge interpretation, our model significantly improves prediction and interpretative prowess. Empirical results validate its efficacy in prediction and interpretation tasks. ExplainMIX's ability to provide meaningful insights into drug response prediction positions it as a valuable tool for precision medicine researchers and beyond.

<br/>
<div align="center">
  <img src="https://github.com/AhauBioinformatics/ExplainMIX/blob/master/picture/overview_img.png" alt="avatar">
</div>
<br/>

In essence, our research comprises two fundamental components. Firstly, we delve into drug response prediction by conceptualizing it as a relational network. This innovative approach allows us to effectively address the inherent heterogeneity within drug response data, making the most of the distinctive features associated with different network nodes. By treating drug response as a relation network phenomenon, we leverage the rich interplay between various nodes, enhancing the overall prediction accuracy.

Secondly, we tackle the crucial challenge of interpreting these predictions. We employ a combination of logical semantic principles and counterfactual reasoning to shed light on the underlying rationale behind our predictions. This interpretive framework not only provides meaningful insights into why a particular prediction was made but also enables us to establish causal links and logical connections within the data.

Furthermore, we evaluate the quality and effectiveness of our interpretation methodology, ensuring that our research doesn't just stop at prediction but extends into the realm of actionable insights. In doing so, we aim to bridge the gap between predictive analytics and practical, real-world applications in the context of drug response prediction.


# Quick start
## Cell line-Drug Prediction
 ```python
    #!/usr/bin/env python3
    import tensorflow as tf
    import RGCN

    #input
    train_triples = np.load('../data/train_triples.npy')
    test_triples = np.load('../data/test_triples.npy')
    entities = np.load(r'../data/entities.npy')

    model = get_RGCN_Model(
        num_entities=NUM_ENTITIES,
        num_relations=NUM_RELATIONS,
        embedding_dim=EMBEDDING_DIM,
        output_dim=OUTPUT_DIM,
        seed=SEED
    )

   # model training
    model.fit(
        x=[
            ALL_INDICES,
            X_train_triples[:,:,0],
            X_train_triples[:,:,1],
            X_train_triples[:,:,2],
            ADJ_MATS
        ],
        y=X_train_triples[:,:, 1].reshape(1, -1),
        epochs=NUM_EPOCHS,
        batch_size=1,
        verbose=1
    )

   # output
   for head, rel, tail, true_exp in tf_data:
        pred = model([
            ALL_INDICES,
            tf.reshape(head, (1, -1)),
            tf.reshape(rel, (1, -1)),
            tf.reshape(tail, (1, -1)),
            ADJ_MATS
        ]
        )
        pred_list.append([head, pred, rel, tail)
   
```


## Prediction Explanations
 ```python
    #!/usr/bin/env python3
    import weight_utils
    import tensorflow as tf

    # The computation of logical semantic graph structures involves the generation and analysis of graph-like
    # representations that capture logical and semantic relationships within data.
    weight_calulate = weight_utils.Weight_Cal()

    train_triples = np.load('../data/train_triples.npy')
    test_triples = np.load('../data/test_triples.npy')
    entities = np.load(r'../data/entities.npy')

    for head, rel, tail , true_exp in tf_data:
        # Tensors can be manually watched by invoking the watch method on this context manager.
        with tf.GradientTape(watch_accessed_variables=False,persistent=True) as tape:
            tape.watch(ADJ_MATS)
        pred_exp = get_pred(ADJ_MATS,NUM_RELATIONS,tape,pred,head,tail,TOP_K)
        for i in range(num_relations):
            gradient_score = tape.gradient(pred, adj_mat_i.values)
            p_logic = weight_calulate.logic_weight(head, tail, pred)
            p_rele = weight_calulate.relevent_weight(head, adj_mat_i.indices[a[0], 2]) 
    
            # The score of the contribution of the relevant edge to the predicted outcome of the interpreted edge   
            score = math.exp(np.sign(pred.numpy())*(p_logic+p_rele))*gradient_score[a][0]
            scores.append(score)
        score_dic = dict(zip(relat, scores))
        top_k_scores = sorted(score_dic.items(), key=lambda x : x[1],reverse=True)[:top_k]



```

# Citation
Ying Xiang, Xiaosong Wang, Qian Gao and Zhenyu Yue*, ExplainMIX: Exploring Drug Response with Explainable Multi-Omics Fusion in Heterogeneous Graph Neural Networks, 2023, Submitted.

# Contact
Please feel free to contact us if you need any help: zhenyuyue@ahau.edu.cn
