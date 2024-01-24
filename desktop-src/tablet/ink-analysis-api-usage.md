---
description: 'There are four layers to the Ink Analysis library: Windows Forms, WPF, COM, and the base layer. This section describes when to use each layer.'
ms.assetid: bd190606-5bd8-4280-ba2b-267588904ed3
title: Ink Analysis API Usage
ms.topic: article
ms.date: 05/31/2018
---

# Ink Analysis API Usage

There are four layers to the Ink Analysis library: Windows Forms, WPF, COM, and the base layer. This section describes when to use each layer.

## Ink Analysis API Overview

The Ink Analysis libraries are designed to be used in a variety of supported programming environments. There are four basic layers through which your application can make use of Ink Analysis. These layers are:

-   The Windows Forms layer
-   The WPF layer
-   The COM layer
-   The base layer

### Windows Forms Applications

You can use the Ink Analysis API in your managed project by adding a reference to the following libraries:

-   Microsoft.Ink.Analysis (Microsoft.Ink.Analysis.dll)
-   Ink Document Analysis Library (IACore.dll)

In Windows Forms applications, you will most likely use the libraries in conjunction with the standard Tablet PC platform objects found in the Microsoft Tablet PC API v1.7 assembly. Be sure you also have a reference to:

-   Microsoft Tablet PC API v1.7.2600.2180 (Microsoft.Ink.dll)

### Windows Presentation Framework Applications

You can use the Ink Analysis API in your WPF project by adding a reference to the Ink Analysis members that are defined in the System.Windows.Ink namespace in the IAWinFX.dll assembly. This assembly is installed by the SDK.

### COM Applications

Non-Automation COM applications should use the COM layer of the Ink Analysis APIs.

Type specific [ContextNode](/previous-versions/ms551996(v=vs.100)) objects-such as [ParagraphNode](/previous-versions/ms580136(v=vs.100)), [InkWordNode](/previous-versions/ms580133(v=vs.100)), and others-are not used in the COM layer. Rather, you should use the [**IContextNode::AddPropertyData**](icontextnode-addpropertydata.md) on the standard [**IContextNode**](icontextnode.md) interface.

You must \#include "IACom.h". You will most likely use the libraries in conjunction wit the Tablet PC platform Ink object, so you should also \#include "msinkaut.h".

### RTS and Other Applications

The Ink Analysis base layer works differently than the others in that it takes point data for analysis rather than [Stroke](/previous-versions/ms552692(v=vs.100)) objects. Examples of where you would work with the Base layer directly rather than using the Windows forms or COM layers include applications that do not use first generation Tablet PC Platform Ink objects, or applications that use the [**RealTimeStylus**](realtimestylus-class.md) APIs to manage stylus input rather than using the Tablet PC Platform [Ink](/previous-versions/ms583670(v=vs.100)) objects.

## 32-bit Support Only

Note that the Ink Analysis libraries are only supported in 32-bit processes.

## Related topics

<dl> <dt>

[Ink Analysis Overview](ink-analysis-overview.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 
