---
description: This attribute measures how far the progress indicator bar is filled.
ms.assetid: d2b64cdf-e0b4-4c92-9cce-7f50753b875f
title: Progress Control Attribute
ms.topic: article
ms.date: 05/31/2018
---

# Progress Control Attribute

This attribute measures how far the progress indicator bar is filled. The record contains two integers and a string. The first number is the progress, the second number is the range (the maximal possible number for the progress). On setting, the integers can be entered as integer fields or strings containing the integers. If the second number is missing it is assumed to be the default (1024). If the progress is larger than the range then it is changed to be the range. The third field is a string, the name of the action whose progress is displayed.

For related information, see [Authoring a ProgressBar Control](authoring-a-progressbar-control.md), and [Adding Custom Actions to the ProgressBar](adding-custom-actions-to-the-progressbar.md).

## Valid Controls

[ProgressBar](progressbar-control.md)

## Associated Bit Flags

This attribute does not use bit flags.

## Remarks

See [Control Attributes](control-attributes.md) and the control you need to create under [Controls](controls.md).

 

 



