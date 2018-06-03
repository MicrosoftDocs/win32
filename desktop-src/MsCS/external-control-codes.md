---
title: External Control Codes
description: External control codes define operations that can be performed on cluster objects. Cluster-aware applications and resource DLLs initiate external control code operations by calling control code functions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 83d3cf61-3a5f-4564-bd8d-3677d103cd12
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- control codes Failover Cluster ,external
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# External Control Codes

External [control codes](about-control-codes.md) define operations that can be performed on [cluster objects](cluster-objects.md). [Cluster-aware applications](cluster-aware-applications.md) and [resource DLLs](resource-dlls.md) initiate external control code operations by calling [control code functions](control-code-functions.md).

Control code functions are general-purpose routines with multiple parameters that provide the framework for control code operations. The configuration and content of these parameters depend on the control code being used. The following pseudocode illustrates the parameters of a control code function.

``` syntax
Return Value = 
ControlCodeFunction
(
    Object Handle,        // for resource types, 2 parameters: cluster handle and resource type name
    Optional Node Handle, 
    Control Code,
    Input Buffer,
    Size of Input Buffer,
    Output Buffer,
    Size of Output Buffer,
    Size of the Resulting Data
);
```

<dl> <dt>

<span id="Object_Handle"></span><span id="object_handle"></span><span id="OBJECT_HANDLE"></span>Object Handle
</dt> <dd>

For all cluster objects except [resource types](resource-types.md), this parameter will be a handle to the cluster object. For resource type, this is two parameters: a cluster handle and the resource type name.

</dd> <dt>

<span id="Optional_Node_Handle"></span><span id="optional_node_handle"></span><span id="OPTIONAL_NODE_HANDLE"></span>Optional Node Handle
</dt> <dd>

If you want to specify a particular [node](nodes.md) to actually perform the operation, pass a handle to that node, otherwise pass **NULL**.

</dd> <dt>

<span id="Control_Code"></span><span id="control_code"></span><span id="CONTROL_CODE"></span>Control Code
</dt> <dd>

The control code for the operation.

</dd> <dt>

<span id="Input_Buffer"></span><span id="input_buffer"></span><span id="INPUT_BUFFER"></span>Input Buffer
</dt> <dd>

Pointer to a buffer containing data required for the operation, or **NULL** if no data is required. Refer to the control code to find out whether data is required and how the data should be formatted. You must allocate and free the memory for the buffer.

</dd> <dt>

<span id="Size_of_Input_Buffer"></span><span id="size_of_input_buffer"></span><span id="SIZE_OF_INPUT_BUFFER"></span>Size of Input Buffer
</dt> <dd>

The size, in bytes, of the input buffer, or 0 if no input is needed.

</dd> <dt>

<span id="Output_Buffer"></span><span id="output_buffer"></span><span id="OUTPUT_BUFFER"></span>Output Buffer
</dt> <dd>

Pointer to a buffer containing data resulting from the operation, or **NULL** if no data is required. You must allocate a buffer and pass it to the function. If the buffer is too small to hold the data, the last parameter ("size of the resulting data" will specify the required size, allowing you to reallocate and try again. Refer to the control code to find out whether data is required and how the data should be formatted.

</dd> <dt>

<span id="Size_of_Output_Buffer"></span><span id="size_of_output_buffer"></span><span id="SIZE_OF_OUTPUT_BUFFER"></span>Size of Output Buffer
</dt> <dd>

The allocated size, in bytes, of the output buffer, or 0 if no output will be generated.

</dd> <dt>

<span id="Size_of_the_Resulting_Data"></span><span id="size_of_the_resulting_data"></span><span id="SIZE_OF_THE_RESULTING_DATA"></span>Size of the Resulting Data
</dt> <dd>

The control code function will specify the size of the data resulting from the operation. If the output buffer was too small to hold the data, use this value to reallocate the buffer and call the function again.

</dd> <dt>

<span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value
</dt> <dd>

Always a **DWORD**, the possible values differ from control code to control code. Refer to the control code for the values to expect.

</dd> </dl>

Some control code operations require input data; others generate output data. The data can take the form of strings, arrays, or more complicated configurations such as [property lists](property-lists.md). What you pass into and expect out of a control code function is determined by the control code.

Therefore, to use a control code in a control code function, you need to know the following:

-   What the control code does.
-   What parameters must accompany the control code.
-   What the possible return values are.

The [Control Code Reference](https://msdn.microsoft.com/library/aa369311) describes this information for each control code. However, there are standard patterns or configurations of parameters that result in a small set of calling conventions. For more information, see [Using Control Codes](using-control-codes.md).

 

 




