---
title: IAgentCharacterEx Listen
description: IAgentCharacterEx Listen
ms.assetid: 8d4cdb6c-04e1-498c-867f-fddbe6e2791a
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx::Listen

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Listen(
   long bListen  // listening mode flag
);
```

Turns Listening mode (speech recognition input) on or off.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bListen"></span><span id="blisten"></span><span id="BLISTEN"></span>*bListen*
</dt> <dd>

Listening mode flag. If this parameter is **True**, the Listening mode is turned on; if **False**, Listening mode is turned off.

</dd> </dl>

Setting this method to **True** enables the Listening mode (turns on speech recognition) for a fixed period of time. While you cannot set the value of the time-out, you can turn off Listening mode before the time-out expires. In addition, if the Listening mode is already on because you (or another client) successfully set the method to **True** before the time-out expires, the method succeeds and resets the time-out. However, if Listening mode is already on because the user is pressing the Listening key, the method succeeds, but the time-out is ignored and the Listening mode ends based on the user's interaction with the Listening key.

This method will succeed only when called by the input-active client. Therefore, the method will fail if your client is not the active client of the topmost character. The method will also fail if you attempt to set the method to **False** and the user is pressing the Listening key. It can also fail if there is no compatible speech engine available that matches the character's language ID setting or the user has disabled speech input using the Microsoft Agent property sheet. However, the method will not fail if the audio device is busy.

When you successfully set this method to **True**, the server triggers the [**IAgentNotifySinkEx::ListeningState**](iagentnotifysinkex--listeningstate.md) event. The server also sends **IAgentNotifySinkEx::ListeningState** when the Listening mode time-out completes or when you set [**IAgentCharacterEx::Listen**](https://www.bing.com/search?q=**IAgentCharacterEx::Listen**) to **False**.

This method does not automatically call [**IAgentCharacter::StopAll**](iagentcharacter--stopall.md) and play a Listening state animation of the character as occurs when the user presses the Listening key. This enables you to use the [**IAgentNotifySinkEx::ListeningState**](iagentnotifysinkex--listeningstate.md) event to determine whether you wish to stop the current animation and play your own appropriate animation. However, once a user utterance is detected, the server automatically calls **IAgentCharacter::StopAll** and plays a Hearing state animation.

## See Also

[**IAgentNotifySinkEx::ListeningState**](iagentnotifysinkex--listeningstate.md), [**IAgentSpeechInputProperties::GetEnabled**](iagentspeechinputproperties--getenabled.md)


 

 




