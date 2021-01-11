---
description: ICE97 verifies that two components do not isolate a shared component to the same directory.
ms.assetid: 76eeb238-02a1-43c1-a3d7-5178e3c3eaee
title: ICE97
ms.topic: article
ms.date: 05/31/2018
---

# ICE97

ICE97 verifies that two components do not isolate a shared component to the same directory.

## Result

ICE97 posts the following warnings.



| ICE97 Warning                                                                                                                                                                    | Description                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| This component \[1\] installs the Shared component into the same directory \[2\] as another, which breaks component rules if both (or more) components are selected for install. | Two components must not isolate a shared component to the same directory. |



 

For example, Component1 and Component2, which share ComponentShared, are installed to the same directory. Both specify ComponentShared as an isolated component. Because of the isolation, the files in ComponentShared are copied twice into the Directory\_ reference for Component1 and Component2. The components now have one reference count on the copy of files. This is in violation of the Installer component rules. If Component1 is uninstalled, the isolated components files are removed and Component2 is broken.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



