---
title: Erasing a Rewritable CD
description: Erasing a Rewritable CD
ms.assetid: 272fdd2b-c174-4bde-b05e-839d547532a6
keywords:
- Windows Media Player,CD burning
- Windows Media Player object model,CD burning
- object model,CD burning
- Windows Media Player ActiveX control,CD burning
- ActiveX control,CD burning
- Windows Media Player Mobile ActiveX control,CD burning
- Windows Media Player Mobile,CD burning
- CD burning,erasing rewritable CDs
- burning CDs,erasing rewritable CDs
- erasing rewritable CDs
ms.topic: article
ms.date: 05/31/2018
---

# Erasing a Rewritable CD

The [IWMPCdromBurn](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcdromburn) interface provides a method for erasing CD-RW discs. Before erasing a CD, you must first ensure that the operation is supported. For more information, see [Retrieving the Drive and Disc Status](retrieving-the-drive-and-disc-status.md).

To begin erasing the contents of a rewritable CD, call [IWMPCdromBurn::erase](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcdromburn-erase).


```C++

    HRESULT hr = m_spCdromBurn->erase();
    

```



## Related topics

<dl> <dt>

[**Burning a CD**](burning-a-cd.md)
</dt> <dt>

[**Retrieving the CD Burning Interface**](retrieving-the-cd-burning-interface.md)
</dt> <dt>

[**Starting the Burn Process**](starting-the-burn-process.md)
</dt> <dt>

[**Retrieving the Drive and Disc Status**](retrieving-the-drive-and-disc-status.md)
</dt> <dt>

[**Retrieving the Burn Status**](retrieving-the-burn-status.md)
</dt> </dl>

 

 




