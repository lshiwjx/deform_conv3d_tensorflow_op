import tensorflow as tf
import numpy as np

deformable_conv3d_grad_module = tf.load_op_library('./deformable_conv3d_grad.so')
offset = [[[[[[1,1,1]]*27]*5]*5]*5] #(1,5,5,5,27,3)
filters = [[[[1,1,1]]*3]*3]
grad = [[[[[1]*3]*3]*3]]
inputs = [[[[[1.]*5]*5]*5]]

with tf.Session(''):
    result = deformable_conv3d_grad_module.deformable_conv3d_grad \
        ( inputs,filters,
       offset,grad
         )[0].eval()
    print(result)


print(grad)
# [[[[1, 0, 0], [0, 0, 0], [0, 0, 0]],  # h1
#   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],  # h2
#   [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]],  # filter clhw  s=1 p=0 out 3*3*3
# [[[[[111, 112, 113, 114, 115], [121, 122, 123, 124, 125], [131, 132, 133, 134, 135], [141, 142, 143, 144, 145], [151, 152, 153, 154, 155]],
#    [[211, 212, 213, 214, 215], [221, 222, 223, 224, 225], [231, 232, 233, 234, 235], [241, 242, 243, 244, 245], [251, 252, 253, 254, 255]],
#    [[311, 312, 313, 314, 315], [321, 322, 323, 324, 325], [331, 332, 333, 334, 335], [341, 342, 343, 344, 345], [351, 352, 353, 354, 355]],
#    [[411, 412, 413, 414, 415], [421, 422, 423, 424, 425], [431, 432, 433, 434, 435], [441, 442, 443, 444, 445], [451, 452, 453, 454, 455]],
#    [[511, 512, 513, 514, 515], [521, 522, 523, 524, 525], [531, 532, 533, 534, 535], [541, 542, 543, 544, 545], [551, 552, 553, 554, 555]]]]],  # input nclhw
#