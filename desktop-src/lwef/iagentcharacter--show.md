---
title: IAgentCharacter Show
description: IAgentCharacter Show
ms.assetid: 5f13dcef-3777-41eb-827f-6162bad71a2e
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::Show

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Show(
   long bFast,      // play Showing state animation flag
   long * pdwReqID  // address of request ID
);
```

Displays a character.

-   Returns S\_OK to indicate the operation was successful. When the function returns, *pdwReqID* contains the ID of the request.

<dl> <dt>

<span id="bFast"></span><span id="bfast"></span><span id="BFAST"></span>*bFast*
</dt> <dd>

Showing state animation flag. If this parameter is **True**, the **Showing** state animation plays after making the character visible; if **False**, the animation does not play.

</dd> <dt>

<span id="pdwReqID"></span><span id="pdwreqid"></span><span id="PDWREQID"></span>*pdwReqID*
</dt> <dd>

Address of a variable that receives the [**Show**](/windows/desktop/lwef/iagentcharacter--show) request ID.

</dd> </dl>

Avoid setting the *bFast* parameter to **True** without playing an animation beforehand, otherwise, the character frame may be displayed, but have no image to display. In particular, note that if you call [**MoveTo**](iagentcharacter--moveto.md) when the character is not visible, it does not play any animation. Therefore, if you call the **Show** method with *bFast* set to **True**, no image will be displayed. Similarly, if you call [**Hide**](/windows/desktop/lwef/iagentcharacter--hide), then **Show** with *bFast* set to **True**, there will be no visible image.

When using the HTTP protocol to access character and animation data, use the [**Prepare**](/windows/desktop/lwef/iagentcharacter--prepare) method to ensure the availability of the **Showing** state animation before calling this method.

## See Also

[**IAgentCharacter::Hide**](iagentcharacter--hide.md)


 

 