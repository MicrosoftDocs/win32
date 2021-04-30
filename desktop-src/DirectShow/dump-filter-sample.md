---
description: Dump Filter Sample
ms.assetid: 2ce52e6c-a02f-4737-822a-87b2cf2d933d
title: Dump Filter Sample
ms.topic: article
ms.date: 05/31/2018
---

# Dump Filter Sample

## Description

The Dump Filter is a renderer filter that writes the media samples it receives to a text file.

This sample illustrates how to use the base filter class [**CBaseFilter**](cbasefilter.md) and the rendered input pin class [**CRenderedInputPin**](crenderedinputpin.md). It also demonstrates how to implement the [**IFileSinkFilter**](/windows/desktop/api/Strmif/nn-strmif-ifilesinkfilter) interface. The Dump filter has a single input pin, which writes every sample that it receives directly to a file.

## Usage

This filter is a useful debugging tool. For example, you can verify, bit by bit, the results of a transform filter. You can build a graph manually by using GraphEdit, and connect the Dump filter to the output of a transform filter or any other output pin. You can also connect a tee filter and put the Dump filter on one leg of the tee filter and the typical output on another leg to monitor the results in a real-time scenario.

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

This sample is installed under the following path: *\[SDK Root\]*\\Samples\\Multimedia\\DirectShow\\Filters\\Dump.

## Related topics

<dl> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> </dl>

 

 



