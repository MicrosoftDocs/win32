---
description: The TRANSFORMS property contains the list of transforms for an installation package. The installer applies all the transforms in the transforms list at every installation, advertisement, installation-on-demand, or maintenance installation of the package.
ms.assetid: dde2ef55-7794-4eb1-984a-ed13e990c97f
title: Applying Transforms
ms.topic: article
ms.date: 05/31/2018
---

# Applying Transforms

The [**TRANSFORMS**](transforms.md) property contains the list of transforms for an installation package. The installer applies all the transforms in the transforms list at every installation, advertisement, installation-on-demand, or maintenance installation of the package.

The [**TRANSFORMS**](transforms.md) property is set by specifying the list of transforms on the command line; however, when using either the /jm or /ju [command line option](command-line-options.md), the transforms list must be specified using the /t option.

Note that the transforms list cannot be modified once installed and can only be removed by uninstalling the application.

> [!Note]  
> A Windows Installer package can apply no more than 255 transforms when installing an application or update. When many transforms are necessary, they should be combined and previous obsolete transforms should be eliminated.

 

The following table provides examples of various transforms strings that could be added to the transforms list.



| Transforms string                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| transform1.mst;:transform2.mst;:transform3.mst                                                                                 | Transform2.mst and transform3.mst are [embedded transforms](embedded-transforms.md). transform1.mst is a [secure-at-source transform](secure-at-source-transforms.md) only if the [**TRANSFORMSSECURE**](transformssecure.md) property or [TransformsSecure policy](transformssecure-policy.md) is set, otherwise transform1 is an [unsecured transform](unsecured-transforms.md). |
| \\\\server\\share\\path\\transform1.mst;:transform2.mst                                                                        | Transform2.mst is an [embedded transform](embedded-transforms.md). transform1.mst is a [secure-full-path transform](secure-full-path-transforms.md) only if the [**TRANSFORMSSECURE**](transformssecure.md) property or [TransformsSecure policy](transformssecure-policy.md) is set, otherwise transform1 is an [unsecured transform](unsecured-transforms.md).                   |
| @:transform2.mst;transform1.mst @transform1.mst;:transform2.mst<br/>                                                     | Transform2.mst is an embedded transform. transform1.mst is a stand-alone [secure-at-source transforms](secure-at-source-transforms.md).                                                                                                                                                                                                                                                |
| \|\\\\server\\share\\path\\transform1.mst;:transform2.mst \|:transform2.mst;\\\\server\\share\\path\\transform1.mst<br/> | Transform2.mst is an embedded transform. transform1.mst is a Standalone [secure-full-path transforms](secure-full-path-transforms.md).                                                                                                                                                                                                                                                 |



 

 

 




