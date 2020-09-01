---
title: GPU acceleration in WSL - FAQ
description: FAQ for GPU acceleration in Windows Subsystem for Linux
ms.topic: article
ms.date: 07/30/2020
---

# FAQ

### Q: How do I enable DirectML acceleration? 

 
The DirectML device is enabled by default, assuming you have an appropriate DirectX 12 GPU available. TensorFlow operations will automatically be assigned to the DirectML device if possible. 

If you're having trouble determining whether your model is running using DirectML acceleration or not, you can put `tf.debugging.set_log_device_placement(True)` as the first statement of your program and TensorFlow will print device placement information to the console.

### Q: How do I control device placement of specific operations? 
 

As with any other device (see [TensorFlow Guide: Use a GPU](https://www.tensorflow.org/guide/gpu)), you can use `tf.device()` to control which device to run on. 
 

The DirectML device string is `'DML'`. 


```python 

import tensorflow as tf 

tf.debugging.set_log_device_placement(True) 

tf.enable_eager_execution() 

 

# Explicitly place tensors on the DirectML device 

with tf.device('/DML:0'): 

  a = tf.constant([1.0, 2.0, 3.0]) 

  b = tf.constant([4.0, 5.0, 6.0]) 

 

c = tf.add(a, b) 

print(c) 

``` 


``` 

Executing op Add in device /job:localhost/replica:0/task:0/device:DML:0 

tf.Tensor([5. 7. 9.], shape=(3,), dtype=float32) 

``` 