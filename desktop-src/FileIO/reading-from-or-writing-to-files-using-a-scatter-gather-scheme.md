---
Description: 'Describes a scatter-gather scheme for reading or writing noncontiguous chunks of data in one operation.'
ms.assetid: 'ae5d83ca-f219-4fcc-ad06-bc242ba95372'
title: 'Reading From or Writing To Files Using a Scatter-Gather Scheme'
---

# Reading From or Writing To Files Using a Scatter-Gather Scheme

A scatter-gather scheme uses the operating system to deliver in one operation multiple discrete chunks of data (such as database records) from a file to separate, noncontiguous buffers in memory. A scatter-gather scheme also writes the data from noncontiguous buffers in one operation.

An application can implement a scatter-gather scheme by using the [**ReadFileScatter**](readfilescatter.md) and [**WriteFileGather**](writefilegather.md) functions.

 

 



