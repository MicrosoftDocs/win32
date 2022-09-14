---
title: Adding Copyright Characters to Metafiles
description: The characters for copyright and trademark registration symbols ( \ 169; or \ 174; ) may not display correctly if the metafile is not encoded using the UTF-8 encoding scheme.
ms.assetid: 9124c8d4-1fc1-4163-ada9-d96af58f8b98
keywords:
- Adding Copyright Characters to Metafiles Windows Media Player
topic_type:
- apiref
api_name:
- Adding Copyright Characters to Metafiles
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Adding Copyright Characters to Metafiles

The characters for copyright and trademark registration symbols ( © or ® ) may not display correctly if the metafile is not encoded using the UTF-8 encoding scheme. In this case, to display either of these symbols properly for all users, you can use the ASCII equivalents (c) and (r) inside the **COPYRIGHT** element, as shown in the following code.


```
<COPYRIGHT>Copyright (c) 1998, Microsoft Corporation</COPYRIGHT>
```



If the metafile is encoded using UTF-8, copyright and trademark symbols will display correctly.

## See also

<dl> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> </dl>

 

 




