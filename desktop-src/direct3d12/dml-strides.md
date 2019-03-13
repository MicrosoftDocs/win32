---
title: Binding in DirectML
description: DirectML tensors are described by properties known as the *sizes* and the *strides* of the tensor.
ms.topic: article
ms.date: 03/12/2019
---

# Using strides to express padding and memory layout

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK). The earliest version in which these feature appears is Windows 10 Insider Preview, version 1903 (10.0; Build 18309).

DirectML tensors&mdash;which are are backed by Direct3D 12 buffers&mdash;are described by properties known as the *sizes* and the *strides* of the tensor. The tensor's *sizes* describe the logical dimensions of the tensor. For example, a 2D tensor might have a height of 2 and a width of 3. Logically, the tensor has 6 distinct elements, although the sizes don't specify how those elements are stored in memory. The tensor's *strides* describe the physical memory layout of the tensor's elements.

## Two-dimensional (2D) arrays

Consider a 2D tensor that has a height of 2 and a width of 3; the data comprises textual characters. In C/C++, this might be expressed using a multi-dimensional array.

```cpp
constexpr int rows = 2;
constexpr int columns = 3;
char tensor[rows][columns];
tensor[0][0] = 'A';
tensor[0][1] = 'B';
tensor[0][2] = 'C';
tensor[1][0] = 'D';
tensor[1][1] = 'E';
tensor[1][2] = 'F';
```

The logical view of the above tensor is visualized below.

```
A B C
D E F
```

In C/C++, a multi-dimensional array is stored in row-major order. In other words, the consecutive elements along the width dimension are stored contiguously in linear memory space.

Offset:|0|1|2|3|4|5
-|-|-|-|-|-|-
Value:|A|B|C|D|E|F

The *stride* of a dimension is the number of elements to skip in order to access the next element in that dimension. Strides express the layout of the tensor in memory. With a row-major order, the stride of the width dimension is always 1, since adjacent elements along the dimension are stored contiguously. The stride of the height dimension depends on the size of the width dimension; in the above example, the distance between consecutive elements along the height dimension (for example, A to D) is equal to the width of the tensor (which is 3 in this example).

To illustrate a different layout, consider column-major order. In other words, the consecutive elements along the height dimension are stored contiguously in linear memory space. In this case, the height-stride is always 1, and the width-stride is 2 (the size of the height dimension).

Offset:|0|1|2|3|4|5
-|-|-|-|-|-|-
Value:|A|D|B|E|C|F

## Higher dimensions

When it comes to greater than two dimensions, it's unwieldy to refer to a layout as either row-major or column-major. So, the rest of this topic uses terms and labels such as these.

- 2D: "HW"&mdash;height is the highest-order dimension (row-major).
- 2D: "WH"&mdash;width is the highest-order dimension (column-major).
- 3D: "DHW"&mdash;depth is the highest-order dimension, followed by height, and then width.
- 3D: "WHD"&mdash;width is the highest-order dimension, followed by height, and then depth.
- 4D: "NCHW"&mdash;the number of images (batch size), then the number of channels, then height, then width.

In general, the *packed* stride of a dimension is equal to the product of the sizes of the lower-order dimensions. For example, with a "DHW" layout, the D-stride is equal to H * W; the H-stride is equal to W; and the W-stride is equal to 1. Strides are said to be *packed* when the total physical size of the tensor is equal to the total logical size of the tensor; in other words, there's no extra space nor overlapping elements.

Let's extend the 2D example to three dimensions, so that we have a tensor with depth 2, height 2, and width 3 (for a total of 12 logical elements).

```
A B C
D E F

G H I
J K L
```

With a "DHW" layout, this tensor is stored as follows.

Offset:|0|1|2|3|4|5|6|7|8|9|10|11|
-|-|-|-|-|-|-|-|-|-|-|-|-|
Value:|A|B|C|D|E|F|G|H|I|J|K|L|

- D-stride = height (2) * width (3) = 6 (for example, the distance between 'A' and 'G').
- H-stride = width (3) = 3 (for example, the distance between 'A' and 'D').
- W-stride = 1 (for example, the distance between 'A' and 'B').

The dot product of the indices/coordinates of an element and the strides provides the offset to that element in the buffer. For example, the offset of the H element (d=1, h=0, w=1) is 7.

{1, 0, 1} ⋅ {6, 3, 1} = 1 * 6 + 0 * 3 + 1 * 1 = 7

## Packed tensors

The examples above illustrate *packed* tensors. A tensor is said to be *packed* when the logical size of the tensor (in elements) is equal to the physical size of the buffer (in elements), and each element has a unique address/offset. For example, a 2x2x3 tensor is packed if the buffer is 12 elements in length and no pair of elements share the same offset in the buffer. Packed tensors are the most common case; but strides allow more complex memory layouts.

## Broadcasting with strides

If a tensor's buffer size (in elements) is smaller than the product of its logical dimensions, then it follows that there must be some overlapping of elements. The usual case for this is known as *broadcasting*; where the elements of a dimension are a duplicate of another dimension. For example, let's revisit the 2D example. Let's say that we want a tensor that is logically 2x3, but the second row is identical to the first row. Here's how that looks.

```
A B C
A B C
```

This could be stored as a packed HW/row-major tensor. But a more compact storage would contain only 3 elements (A, B, and C) and use a height-stride of 0 instead of 3. In this case, the physical size of the tensor is 3 elements, but the logical size is 6 elements.

In general, if the stride of a dimension is 0, then all elements in the lower-order dimensions are repeated along the broadcasted dimension; for example, if the tensor is NCHW and the C-stride is 0, then each channel has the same values along H and W.

## Padding with strides

A tensor is said to be *padded* if its physical size is larger than the minimum size needed to fit its elements. When there is no broadcasting nor overlapping elements, the minimum size of the tensor (in elements) is simply the product of its dimensions. You can use the helper function `DMLCalcBufferTensorSize` (see [DirectML helper functions](dml-helper-functions.md) for a listing of that function) to calculate the *minimum* buffer size for your DirectML tensors.

Let's say that a buffer contains the following values (the 'x' elements indicate padding values).

0|1|2|3|4|5|6|7|8|9|
-|-|-|-|-|-|-|-|-|-|
A|B|C|x|x|D|E|F|x|x

The padded tensor can be described by using a height-stride of 5 instead of 3. Instead of stepping by 3 elements to get to the next row, the step is 5 elements (3 *real* elements plus 2 padding elements). Padding is common in computer graphics, for example, to ensure that an image has a power-of-two alignment.

```
A B C
D E F
```

## DirectML buffer tensor descriptions

DirectML can work with a variety of physical tensor layouts, since the [**DML_BUFFER_TENSOR_DESC** structure](/windows/desktop/api/directml/ns-directml-dml_buffer_tensor_desc) has both `Sizes` and `Strides` members. Some operator implementations might be more efficient with a specific layout, so it's not uncommon to change how tensor data is stored for better performance.

Most DirectML operators require either 4D or 5D tensors, and the order of the sizes and strides values is fixed. By fixing the order of the sizes and stride values in a tensor description, it's possible for DirectML to infer different physical layouts.

**4D**
- [**DML_BUFFER_TENSOR_DESC::Sizes**](/windows/desktop/api/directml/ns-directml-dml_buffer_tensor_desc) = { N-size, C-size, H-size, W-size }
- [**DML_BUFFER_TENSOR_DESC::Strides**](/windows/desktop/api/directml/ns-directml-dml_buffer_tensor_desc) = { N-stride, C-stride, H-stride, W-stride }

**5D**
- **DML_BUFFER_TENSOR_DESC::Sizes** = { N-size, C-size, D-size, H-size, W-size }
- **DML_BUFFER_TENSOR_DESC::Strides** = { N-stride, C-stride, D-stride, H-stride, W-stride }

If a DirectML operator requires a 4D or a 5D tensor, but the actual data has a smaller rank (for example, 2D), then the leading dimensions should be filled with 1s. For example, an "HW" tensor is set using **DML_BUFFER_TENSOR_DESC::Sizes** = { 1, 1, H, W }.

If tensor data is stored in NCHW/NCDHW, then it's not necessary to set **DML_BUFFER_TENSOR_DESC::Strides**, unless you want broadcasting or padding. You can set the strides field to `nullptr`. However, if the tensor data is stored in another layout, such as NHWC, then you need strides in order to express the transformation from NCHW to that layout.

For a simple example, consider the description of a 2D tensor with height 3 and width 5.

**Packed NCHW (implicit strides)**
- **DML_BUFFER_TENSOR_DESC::Sizes** = { 1, 1, 3, 5 }
- **DML_BUFFER_TENSOR_DESC::Strides** = `nullptr`

**Packed NCHW (explicit strides)**
- N-stride = C-size * H-size * W-size = 1 * 3 * 5 = 15
- C-stride = H-size * W-size = 3 * 5 = 15
- H-stride = W-size = 5
- W-stride = 1
- **DML_BUFFER_TENSOR_DESC::Sizes** = { 1, 1, 3, 5 }
- **DML_BUFFER_TENSOR_DESC::Strides** = { 15, 15, 5, 1 }

**Packed NHWC**
- N-stride = H-size * W-size * C-size = 3 * 5 * 1 = 15
- H-stride = W-size * C-size = 5 * 1 = 5
- W-stride = C-size = 1
- C-stride = 1
- **DML_BUFFER_TENSOR_DESC::Sizes** = { 1, 1, 3, 5 }
- **DML_BUFFER_TENSOR_DESC::Strides** = { 15, 1, 5, 1 }

## See also

* [DirectML helper functions](dml-helper-functions.md)
* [DML_BUFFER_TENSOR_DESC structure](/windows/desktop/api/directml/ns-directml-dml_buffer_tensor_desc)
