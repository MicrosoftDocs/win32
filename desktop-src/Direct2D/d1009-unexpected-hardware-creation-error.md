---
title: D1009 Unexpected Hardware Creation Error
description: An unexpected error \ error\ was encountered while trying to create a Direct3D target.
ms.assetid: 1ff34b1f-0ab3-4821-97f5-a4e67831383a
keywords:
- D1009 Unexpected Hardware Creation Error Direct2D
topic_type:
- apiref
api_name:
- D1009 Unexpected Hardware Creation Error
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# D1009: Unexpected Hardware Creation Error

An unexpected error \[*error*\] was encountered while trying to create a Direct3D target.

## Placeholders

<dl> <dt>

<span id="error"></span><span id="ERROR"></span>*error*
</dt> <dd>

An error number.

</dd> </dl> 

| &nbsp;      |  &nbsp; |
|-------------|---------|
| Error Level | Warning |



 

## Possible Causes

-   The target was larger than the maximum bitmap size.
-   Out of video memory as the render target is created.
-   No Direct3D device could be created.
-   The application is running on IA64.

 

 




