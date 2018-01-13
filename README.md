# AMSGrad

This is a Tensorflow implementation of the AMSGrad algorithm in the ICLR 2018 submission "On the Convergence of Adam and Beyond". Have fun.

## Usage
```python
import optimizers

# just like tf.train.AdamOptimizer(learning_rate=0.01), you can specify
opt = optimizers.AMSGrad(learning_rate=0.01)
# and you are ready to go
```

## Test Environment / Prerequisites
- Python 2.7
- Tensorflow 1.4
- Matplotlib

## Toy Experiment

There is a toy experiment in `toy.ipynb`. This experiment is (almost) the same as in the paper, except that here we do not have the `[-1,1]` constraint. The results indeed show that AMSGrad can move towards `-inf` while Adam cannot.

## MNIST Experiment

As in `mnist_f_f.ipynb`, it is a 784-100-10 fully connected network. However, I could not replicate the results in the paper, possibly because I use different hyperparameters.
