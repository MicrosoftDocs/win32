---
title: Miscellaneous Status Bits Support
description: Miscellaneous Status Bits Support
ms.assetid: 3f967371-3d5a-4948-9008-6f4c3052bf07
ms.topic: article
ms.date: 05/31/2018
---

# Miscellaneous Status Bits Support

ActiveX Control Containers must recognize and support the following OLEMISC\_ status bits.



| Status Bit                           | Required?      | Comments                                                                                                                                                                                                                                                                                                |
|--------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACTIVATEWHENVISIBLE<br/>       | Yes<br/> |                                                                                                                                                                                                                                                                                                         |
| IGNOREACTIVATEWHENVISIBLE<br/> | No<br/>  | Needed for inactive and windowless control support. The IGNOREACTIVATEWHENVISIBLE bit is for containers hosting inactive and windowless controls. The IGNOREACTIVATEWHENVISIBLE bit is introduced as part of the ActiveX Controls 96 specification, see this documentation for more details.<br/> |
| INSIDEOUT<br/>                 | No<br/>  | Not generally used with ActiveX Controls but rather with compound document embeddings. Note this is contrary to some SDK documentation that says this bit must be set for the ACTIVATEWHENVISIBLE bit to be set.<br/>                                                                             |
| INVISIBLEATRUNTIME<br/>        | Yes<br/> | Designates a control that should be visible at design time, but invisible at run time.<br/>                                                                                                                                                                                                       |
| ALWAYSRUN<br/>                 | Yes<br/> |                                                                                                                                                                                                                                                                                                         |
| ACTSLIKEBUTTON<br/>            | No<br/>  | Support is normally mandatory although it is not necessary for document style containers.<br/>                                                                                                                                                                                                    |
| ACTSLIKELABEL<br/>             | No<br/>  | Support is normally mandatory although it is not necessary for document style containers.<br/>                                                                                                                                                                                                    |
| NOUIACTIVATE<br/>              | Yes<br/> |                                                                                                                                                                                                                                                                                                         |
| ALIGNABLE<br/>                 | No<br/>  |                                                                                                                                                                                                                                                                                                         |
| SIMPLEFRAME<br/>               | No<br/>  | See [Simple Frame Site Containment](simple-frame-site-containment.md)<br/>                                                                                                                                                                                                                       |
| SETCLIENTSITEFIRST<br/>        | No<br/>  | Support for this bit is recommended but not mandatory.<br/>                                                                                                                                                                                                                                       |
| IMEMODE<br/>                   | No<br/>  |                                                                                                                                                                                                                                                                                                         |



 

## Related topics

<dl> <dt>

[Containers](containers.md)
</dt> </dl>

 

 





