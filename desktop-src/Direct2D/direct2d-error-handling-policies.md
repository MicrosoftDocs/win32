---
title: Direct2D Error Handling Policies
description: This topic describes the Direct2D error handling policies. It contains the following sections.
ms.assetid: b5fa327a-a315-46fa-aa78-8a5733faae01
keywords:
- Direct2D,error handling
ms.topic: article
ms.date: 05/31/2018
---

# Direct2D Error Handling Policies

This topic describes the Direct2D error handling policies. It contains the following sections.

-   [Use of HRESULT](#use-of-hresult)
-   [Return Value of Batched Functions](#return-value-of-batched-functions)
-   [Invalid Input](#invalid-input)
    -   [Output Pointer](#output-pointer)
    -   [Required Parameter](#required-parameter)
-   [NaN and Poorly Ordered Input RECTs](#nan-and-poorly-ordered-input-rects)
    -   [NaN as Input](#nan-as-input)
    -   [Poorly Ordered Input RECTs](#poorly-ordered-input-rects)

## Use of HRESULT

If a function is not batched and can have a run-time failure, it should return **HRESULT** to indicate a failure. A run-time failure is any failure that cannot be avoided at design time, such as out of memory.

## Return Value of Batched Functions

Batched functions in Direct2D are the functions that are processed as a single unit when [**EndDraw**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-enddraw) or [**Close**](/windows/win32/api/d2d1/nf-d2d1-id2d1simplifiedgeometrysink-close) is called. They are the drawing commands between [**BeginDraw**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-begindraw) and **EndDraw** or commands on [**GeometrySink**](/windows/win32/api/d2d1/nn-d2d1-id2d1geometrysink). For these functions, errors are reported at the time the batch is completed. The error is returned after **EndDraw** for drawing commands, and after **Close** for **GeometrySink**.

RenderTargets stop drawing if an error state is set, but an application can call [**Flush**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-flush) to reset the error state and resume drawing.

**Get** and **Set** functions have no return value. However, if a **Set** function has an invalid input, the debug layer generates a message. In this case, no error state is set and the **Set** function does nothing.

## Invalid Input

Direct2D dereferences output pointers and required parameters which result in access violations when the pointers are invalid or **NULL**.

### Output Pointer

Direct2D dereferences an output pointer and assigns it to **NULL** immediately upon entering the function. This causes an access violation if a caller passes in **NULL** as the pointer to the return value. This policy also applies to arrays of pointers. For other output parameters, such as a struct, the dereference happens later and also results in an access violation. However, there are some methods that have optional output pointers (that is, [**EndDraw**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-enddraw), [**Flush**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-flush)) that will not cause an access violation.

### Required Parameter

If **NULL** is passed to any function requiring a valid value, the function dereferences the bad pointer early resulting in an access violation. For optional input parameters, **NULL** is a valid value that results in some reasonable default.

## NaN and Poorly Ordered Input RECTs

In Direct2D, NaN is considered a valid input and poorly ordered input RECTs are sorted.

### NaN as Input

NaN is considered a valid input, though it typically results in the primitive that contains the NaN not drawing. The Direct2D API does not provide explicit filtering of NaN to validate input.

### Poorly Ordered Input RECTs

Poorly ordered input RECTs are sorted so that the top, left and bottom, right corners are correctly specified. For output, empty rectangles look like this: {Infinity, Infinity, FloatMax, FloatMax}.

 

 