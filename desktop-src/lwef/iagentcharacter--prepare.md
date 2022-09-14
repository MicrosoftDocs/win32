---
title: IAgentCharacter Prepare
description: IAgentCharacter Prepare
ms.assetid: e016039f-a0b1-4ae9-bff6-7212b02c1ad8
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::Prepare

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Prepare(
   long dwType,     // type of animation data to load
   BSTR bszName,    // name of the animation 
   long bQueue,     // queue the request
   long * pdwReqID  // address of request ID
);
```

Retrieves animation data for a character.

-   Returns S\_OK to indicate the operation was successful. When the function returns, *pdwReqID* contains the ID of the request.

<dl> <dt>

<span id="dwType"></span><span id="dwtype"></span><span id="DWTYPE"></span>*dwType*
</dt> <dd>

A value that indicates the animation data type to load that must be one of the following:



| Value                                                           | Description                                                |
|-----------------------------------------------------------------|------------------------------------------------------------|
| **const unsigned short** **PREPARE\_ANIMATION = 0;**<br/> | A character's animation data.                              |
| **const unsigned short** **PREPARE\_STATE = 1;**<br/>     | A character's state data.                                  |
| **const unsigned short** **PREPARE\_WAVE = 2**<br/>       | A character's sound file (.WAV or .LWV) for spoken output. |



 

</dd> <dt>

<span id="bszName"></span><span id="bszname"></span><span id="BSZNAME"></span>*bszName*
</dt> <dd>

The name of the animation or state.

The animation name is based on that defined for the character when it was saved using the Microsoft Agent Character Editor.

For states, the value can be one of the following:



|                      | Description                                     |
|----------------------|-------------------------------------------------|
| **"Gesturing"**      | To retrieve all **Gesturing** state animations. |
| **"GesturingDown"**  | To retrieve **GesturingDown** animations.       |
| **"GesturingLeft"**  | To retrieve **GesturingLeft** animations.       |
| **"GesturingRight"** | To retrieve **GesturingRight** animations.      |
| **"GesturingUp"**    | To retrieve **GesturingUp** animations.         |
| **"Hiding"**         | To retrieve the **Hiding** state animations.    |
| **"Hearing"**        | To retrieve the **Hearing** state animations.   |
| **"Idling"**         | To retrieve all **Idling** state animations.    |
| **"IdlingLevel1"**   | To retrieve all **IdlingLevel1** animations.    |
| **"IdlingLevel2"**   | To retrieve all **IdlingLevel2** animations.    |
| **"IdlingLevel3"**   | To retrieve all **IdlingLevel3** animations.    |
| **"Listening"**      | To retrieve the **Listening** state animations. |
| **"Moving"**         | To retrieve all **Moving** state animations.    |
| **"MovingDown"**     | To retrieve all **Moving** animations.          |
| **"MovingLeft"**     | To retrieve all **MovingLeft** animations.      |
| **"MovingRight"**    | To retrieve all **MovingRight** animations.     |
| **"MovingUp"**       | To retrieve all **MovingUp** animations.        |
| **"Showing"**        | To retrieve the **Showing** state animations.   |
| **"Speaking"**       | To retrieve the **Speaking** state animations.  |



 

For .WAV files, set *bszName* to the URL or file specification for the .WAV file. If the specification is not complete, it is interpreted as being relative to the specification used in the [**Load**](https://www.bing.com/search?q=**Load**) method.

</dd> <dt>

<span id="bQueue"></span><span id="bqueue"></span><span id="BQUEUE"></span>*bQueue*
</dt> <dd>

A Boolean specifying whether the server queues the [**Prepare**](/windows/desktop/lwef/iagentcharacter--prepare) request. **True** queues the request and causes any animation request that follows it to wait until the animation data it specifies is loaded. **False** retrieves the animation data asynchronously.

</dd> <dt>

<span id="pdwReqID"></span><span id="pdwreqid"></span><span id="PDWREQID"></span>*pdwReqID*
</dt> <dd>

Address of a variable that receives the [**Prepare**](/windows/desktop/lwef/iagentcharacter--prepare) request ID.

</dd> </dl>

If you load a character using the HTTP protocol (an .ACF file), you must use the [**Prepare**](/windows/desktop/lwef/iagentcharacter--prepare) method to retrieve animation data before you can play the animation. You cannot use this method if you loaded the character using the UNC protocol (an .ACS file). You also cannot retrieve HTTP data for a character using **Prepare** if you loaded that character using the UNC protocol (.ACS character file).

Animation or sound data retrieved with the [**Prepare**](/windows/desktop/lwef/iagentcharacter--prepare) method is stored in the browser's cache. Subsequent calls will check the cache, and if the animation data is already there, the control loads the data directly from the cache. Once loaded, the animation or sound data can be played with the [**Play**](/windows/desktop/lwef/iagentcharacter--play) or [**Speak**](/windows/desktop/lwef/iagentcharacter--speak) methods.

You can specify multiple animations and states by separating them with commas. However, you cannot mix types in the same [**Prepare**](/windows/desktop/lwef/iagentcharacter--prepare) statement.

 

