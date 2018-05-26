---
Description: Describes a scatter-gather scheme for reading or writing noncontiguous chunks of data in one operation.
ms.assetid: ae5d83ca-f219-4fcc-ad06-bc242ba95372
title: Reading From or Writing To Files Using a Scatter-Gather Scheme
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Reading From or Writing To Files Using a Scatter-Gather Scheme

A scatter-gather scheme uses the operating system to deliver in one operation multiple discrete chunks of data (such as database records) from a file to separate, noncontiguous buffers in memory. A scatter-gather scheme also writes the data from noncontiguous buffers in one operation.

An application can implement a scatter-gather scheme by using the [**ReadFileScatter**](/windows/win32/FileAPI/nf-fileapi-readfilescatter?branch=master) and [**WriteFileGather**](/windows/win32/FileAPI/nf-fileapi-writefilegather?branch=master) functions.

 

 



