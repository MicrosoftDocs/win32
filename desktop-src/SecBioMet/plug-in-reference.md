---
title: Plug-in Reference
description: Adapter functions, wrapper functions, and structures for creating custom plug-in adapters of three types engine, sensor, and storage.
ms.assetid: 1886c389-b914-4b2d-ab7e-3e163782673d
keywords:
- Windows Biometric Framework API Windows Biometric Framework API , plug-in reference
ms.topic: article
ms.date: 05/31/2018
---

# Plug-in Reference

Biometric devices are manufactured in a wide variety of types and configurations. The Windows Biometric Framework incorporates an extensible architecture that enables you to deal with this variety by creating custom plug-ins. At the center of this architecture is a software object called a biometric unit. You can think of a biometric unit as an abstraction that represents a biometric device to the Framework. Plug-in software components called adapters connect the biometric unit to the associated hardware. There are three types of adapters that you can create. An engine adapter generates biometric templates from captured samples, matches samples to existing templates, and indexes templates. A sensor adapter wraps a biometric device and provides a standard interface for configuring the sensor, capturing samples, and controlling the flow of biometric data to the processing engine. A storage adapter manages template databases.

## In this section



| Topic                                                                 | Description                                                                                                                                                        |
|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Plug-in Functions](plug-in-functions.md)<br/>                 | Functions you can use to create the adapter plug-ins that make up a biometric unit.<br/>                                                                     |
| [Plug-in Structures](plug-in-structures.md)<br/>               | Structures for client application development by the Windows Biometric Framework API.<br/>                                                                   |
| [Plug-in Wrapper Functions](plug-in-wrapper-functions.md)<br/> | Wrapper functions that allow you to call a public function on any adapter attached to the pipeline without manually acquiring a pointer to the adapter.<br/> |



 

 

 





