---
title: WM_APPCOMMAND message (Winuser.h)
description: Notifies a window that the user generated an application command event, for example, by clicking an application command button using the mouse or typing an application command key on the keyboard.
ms.assetid: ffcdfc44-dbfa-42d4-8749-b33bf0e4de0c
keywords:
- WM_APPCOMMAND message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_APPCOMMAND
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_APPCOMMAND message

Notifies a window that the user generated an application command event, for example, by clicking an application command button using the mouse or typing an application command key on the keyboard.


```C++
#define WM_APPCOMMAND                   0x0319
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the window where the user clicked the button or pressed the key. This can be a child window of the window receiving the message. For more information about processing this message, see the Remarks section.

</dd> <dt>

*lParam* 
</dt> <dd>

Use the following code to get the information contained in the *lParam* parameter.


```
cmd  = GET_APPCOMMAND_LPARAM(lParam);

uDevice = GET_DEVICE_LPARAM(lParam);

dwKeys = GET_KEYSTATE_LPARAM(lParam);
```



The application command is *cmd*, which can be one of the following values.



| Value                                                                                                                                                                                                                                                                                                                  | Meaning                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="APPCOMMAND_BASS_BOOST"></span><span id="appcommand_bass_boost"></span><dl> <dt>**APPCOMMAND\_BASS\_BOOST**</dt> <dt>20</dt> </dl>                                                                         | Toggle the bass boost on and off.<br/>                                                                                                                                                                                                                                               |
| <span id="APPCOMMAND_BASS_DOWN"></span><span id="appcommand_bass_down"></span><dl> <dt>**APPCOMMAND\_BASS\_DOWN**</dt> <dt>19</dt> </dl>                                                                            | Decrease the bass.<br/>                                                                                                                                                                                                                                                              |
| <span id="APPCOMMAND_BASS_UP"></span><span id="appcommand_bass_up"></span><dl> <dt>**APPCOMMAND\_BASS\_UP**</dt> <dt>21</dt> </dl>                                                                                  | Increase the bass.<br/>                                                                                                                                                                                                                                                              |
| <span id="APPCOMMAND_BROWSER_BACKWARD"></span><span id="appcommand_browser_backward"></span><dl> <dt>**APPCOMMAND\_BROWSER\_BACKWARD**</dt> <dt>1</dt> </dl>                                                        | Navigate backward.<br/>                                                                                                                                                                                                                                                              |
| <span id="APPCOMMAND_BROWSER_FAVORITES"></span><span id="appcommand_browser_favorites"></span><dl> <dt>**APPCOMMAND\_BROWSER\_FAVORITES**</dt> <dt>6</dt> </dl>                                                     | Open favorites.<br/>                                                                                                                                                                                                                                                                 |
| <span id="APPCOMMAND_BROWSER_FORWARD"></span><span id="appcommand_browser_forward"></span><dl> <dt>**APPCOMMAND\_BROWSER\_FORWARD**</dt> <dt>2</dt> </dl>                                                           | Navigate forward.<br/>                                                                                                                                                                                                                                                               |
| <span id="APPCOMMAND_BROWSER_HOME"></span><span id="appcommand_browser_home"></span><dl> <dt>**APPCOMMAND\_BROWSER\_HOME**</dt> <dt>7</dt> </dl>                                                                    | Navigate home.<br/>                                                                                                                                                                                                                                                                  |
| <span id="APPCOMMAND_BROWSER_REFRESH"></span><span id="appcommand_browser_refresh"></span><dl> <dt>**APPCOMMAND\_BROWSER\_REFRESH**</dt> <dt>3</dt> </dl>                                                           | Refresh page.<br/>                                                                                                                                                                                                                                                                   |
| <span id="APPCOMMAND_BROWSER_SEARCH"></span><span id="appcommand_browser_search"></span><dl> <dt>**APPCOMMAND\_BROWSER\_SEARCH**</dt> <dt>5</dt> </dl>                                                              | Open search.<br/>                                                                                                                                                                                                                                                                    |
| <span id="APPCOMMAND_BROWSER_STOP"></span><span id="appcommand_browser_stop"></span><dl> <dt>**APPCOMMAND\_BROWSER\_STOP**</dt> <dt>4</dt> </dl>                                                                    | Stop download.<br/>                                                                                                                                                                                                                                                                  |
| <span id="APPCOMMAND_CLOSE"></span><span id="appcommand_close"></span><dl> <dt>**APPCOMMAND\_CLOSE**</dt> <dt>31</dt> </dl>                                                                                         | Close the window (not the application).<br/>                                                                                                                                                                                                                                         |
| <span id="APPCOMMAND_COPY"></span><span id="appcommand_copy"></span><dl> <dt>**APPCOMMAND\_COPY**</dt> <dt>36</dt> </dl>                                                                                            | Copy the selection.<br/>                                                                                                                                                                                                                                                             |
| <span id="APPCOMMAND_CORRECTION_LIST"></span><span id="appcommand_correction_list"></span><dl> <dt>**APPCOMMAND\_CORRECTION\_LIST**</dt> <dt>45</dt> </dl>                                                          | Brings up the correction list when a word is incorrectly identified during speech input. <br/>                                                                                                                                                                                       |
| <span id="APPCOMMAND_CUT"></span><span id="appcommand_cut"></span><dl> <dt>**APPCOMMAND\_CUT**</dt> <dt>37</dt> </dl>                                                                                               | Cut the selection.<br/>                                                                                                                                                                                                                                                              |
| <span id="APPCOMMAND_DICTATE_OR_COMMAND_CONTROL_TOGGLE"></span><span id="appcommand_dictate_or_command_control_toggle"></span><dl> <dt>**APPCOMMAND\_DICTATE\_OR\_COMMAND\_CONTROL\_TOGGLE**</dt> <dt>43</dt> </dl> | Toggles between two modes of speech input: dictation and command/control (giving commands to an application or accessing menus). <br/>                                                                                                                                               |
| <span id="APPCOMMAND_FIND"></span><span id="appcommand_find"></span><dl> <dt>**APPCOMMAND\_FIND**</dt> <dt>28</dt> </dl>                                                                                            | Open the **Find** dialog.<br/>                                                                                                                                                                                                                                                       |
| <span id="APPCOMMAND_FORWARD_MAIL"></span><span id="appcommand_forward_mail"></span><dl> <dt>**APPCOMMAND\_FORWARD\_MAIL**</dt> <dt>40</dt> </dl>                                                                   | Forward a mail message.<br/>                                                                                                                                                                                                                                                         |
| <span id="APPCOMMAND_HELP"></span><span id="appcommand_help"></span><dl> <dt>**APPCOMMAND\_HELP**</dt> <dt>27</dt> </dl>                                                                                            | Open the **Help** dialog.<br/>                                                                                                                                                                                                                                                       |
| <span id="APPCOMMAND_LAUNCH_APP1"></span><span id="appcommand_launch_app1"></span><dl> <dt>**APPCOMMAND\_LAUNCH\_APP1**</dt> <dt>17</dt> </dl>                                                                      | Start App1.<br/>                                                                                                                                                                                                                                                                     |
| <span id="APPCOMMAND_LAUNCH_APP2"></span><span id="appcommand_launch_app2"></span><dl> <dt>**APPCOMMAND\_LAUNCH\_APP2**</dt> <dt>18</dt> </dl>                                                                      | Start App2.<br/>                                                                                                                                                                                                                                                                     |
| <span id="APPCOMMAND_LAUNCH_MAIL"></span><span id="appcommand_launch_mail"></span><dl> <dt>**APPCOMMAND\_LAUNCH\_MAIL**</dt> <dt>15</dt> </dl>                                                                      | Open mail.<br/>                                                                                                                                                                                                                                                                      |
| <span id="APPCOMMAND_LAUNCH_MEDIA_SELECT"></span><span id="appcommand_launch_media_select"></span><dl> <dt>**APPCOMMAND\_LAUNCH\_MEDIA\_SELECT**</dt> <dt>16</dt> </dl>                                             | Go to Media Select mode.<br/>                                                                                                                                                                                                                                                        |
| <span id="APPCOMMAND_MEDIA_CHANNEL_DOWN"></span><span id="appcommand_media_channel_down"></span><dl> <dt>**APPCOMMAND\_MEDIA\_CHANNEL\_DOWN**</dt> <dt>52</dt> </dl>                                                | Decrement the channel value, for example, for a TV or radio tuner. <br/>                                                                                                                                                                                                             |
| <span id="APPCOMMAND_MEDIA_CHANNEL_UP"></span><span id="appcommand_media_channel_up"></span><dl> <dt>**APPCOMMAND\_MEDIA\_CHANNEL\_UP**</dt> <dt>51</dt> </dl>                                                      | Increment the channel value, for example, for a TV or radio tuner. <br/>                                                                                                                                                                                                             |
| <span id="APPCOMMAND_MEDIA_FAST_FORWARD"></span><span id="appcommand_media_fast_forward"></span><dl> <dt>**APPCOMMAND\_MEDIA\_FAST\_FORWARD**</dt> <dt>49</dt> </dl>                                                | Increase the speed of stream playback. This can be implemented in many ways, for example, using a fixed speed or toggling through a series of increasing speeds. <br/>                                                                                                               |
| <span id="APPCOMMAND_MEDIA_NEXTTRACK"></span><span id="appcommand_media_nexttrack"></span><dl> <dt>**APPCOMMAND\_MEDIA\_NEXTTRACK**</dt> <dt>11</dt> </dl>                                                          | Go to next track.<br/>                                                                                                                                                                                                                                                               |
| <span id="APPCOMMAND_MEDIA_PAUSE"></span><span id="appcommand_media_pause"></span><dl> <dt>**APPCOMMAND\_MEDIA\_PAUSE**</dt> <dt>47</dt> </dl>                                                                      | Pause. If already paused, take no further action. This is a direct PAUSE command that has no state. If there are discrete Play and Pause buttons, applications should take action on this command as well as **APPCOMMAND\_MEDIA\_PLAY\_PAUSE**. <br/>                               |
| <span id="APPCOMMAND_MEDIA_PLAY"></span><span id="appcommand_media_play"></span><dl> <dt>**APPCOMMAND\_MEDIA\_PLAY**</dt> <dt>46</dt> </dl>                                                                         | Begin playing at the current position. If already paused, it will resume. This is a direct PLAY command that has no state. If there are discrete **Play** and **Pause** buttons, applications should take action on this command as well as **APPCOMMAND\_MEDIA\_PLAY\_PAUSE**.<br/> |
| <span id="APPCOMMAND_MEDIA_PLAY_PAUSE"></span><span id="appcommand_media_play_pause"></span><dl> <dt>**APPCOMMAND\_MEDIA\_PLAY\_PAUSE**</dt> <dt>14</dt> </dl>                                                      | Play or pause playback. If there are discrete **Play** and **Pause** buttons, applications should take action on this command as well as **APPCOMMAND\_MEDIA\_PLAY** and **APPCOMMAND\_MEDIA\_PAUSE**.<br/>                                                                          |
| <span id="APPCOMMAND_MEDIA_PREVIOUSTRACK"></span><span id="appcommand_media_previoustrack"></span><dl> <dt>**APPCOMMAND\_MEDIA\_PREVIOUSTRACK**</dt> <dt>12</dt> </dl>                                              | Go to previous track.<br/>                                                                                                                                                                                                                                                           |
| <span id="APPCOMMAND_MEDIA_RECORD"></span><span id="appcommand_media_record"></span><dl> <dt>**APPCOMMAND\_MEDIA\_RECORD**</dt> <dt>48</dt> </dl>                                                                   | Begin recording the current stream.<br/>                                                                                                                                                                                                                                             |
| <span id="APPCOMMAND_MEDIA_REWIND"></span><span id="appcommand_media_rewind"></span><dl> <dt>**APPCOMMAND\_MEDIA\_REWIND**</dt> <dt>50</dt> </dl>                                                                   | Go backward in a stream at a higher rate of speed. This can be implemented in many ways, for example, using a fixed speed or toggling through a series of increasing speeds. <br/>                                                                                                   |
| <span id="APPCOMMAND_MEDIA_STOP"></span><span id="appcommand_media_stop"></span><dl> <dt>**APPCOMMAND\_MEDIA\_STOP**</dt> <dt>13</dt> </dl>                                                                         | Stop playback.<br/>                                                                                                                                                                                                                                                                  |
| <span id="APPCOMMAND_MIC_ON_OFF_TOGGLE"></span><span id="appcommand_mic_on_off_toggle"></span><dl> <dt>**APPCOMMAND\_MIC\_ON\_OFF\_TOGGLE**</dt> <dt>44</dt> </dl>                                                  | Toggle the microphone.<br/>                                                                                                                                                                                                                                                          |
| <span id="APPCOMMAND_MICROPHONE_VOLUME_DOWN"></span><span id="appcommand_microphone_volume_down"></span><dl> <dt>**APPCOMMAND\_MICROPHONE\_VOLUME\_DOWN**</dt> <dt>25</dt> </dl>                                    | Decrease microphone volume.<br/>                                                                                                                                                                                                                                                     |
| <span id="APPCOMMAND_MICROPHONE_VOLUME_MUTE"></span><span id="appcommand_microphone_volume_mute"></span><dl> <dt>**APPCOMMAND\_MICROPHONE\_VOLUME\_MUTE**</dt> <dt>24</dt> </dl>                                    | Mute the microphone.<br/>                                                                                                                                                                                                                                                            |
| <span id="APPCOMMAND_MICROPHONE_VOLUME_UP"></span><span id="appcommand_microphone_volume_up"></span><dl> <dt>**APPCOMMAND\_MICROPHONE\_VOLUME\_UP**</dt> <dt>26</dt> </dl>                                          | Increase microphone volume.<br/>                                                                                                                                                                                                                                                     |
| <span id="APPCOMMAND_NEW"></span><span id="appcommand_new"></span><dl> <dt>**APPCOMMAND\_NEW**</dt> <dt>29</dt> </dl>                                                                                               | Create a new window.<br/>                                                                                                                                                                                                                                                            |
| <span id="APPCOMMAND_OPEN"></span><span id="appcommand_open"></span><dl> <dt>**APPCOMMAND\_OPEN**</dt> <dt>30</dt> </dl>                                                                                            | Open a window.<br/>                                                                                                                                                                                                                                                                  |
| <span id="APPCOMMAND_PASTE"></span><span id="appcommand_paste"></span><dl> <dt>**APPCOMMAND\_PASTE**</dt> <dt>38</dt> </dl>                                                                                         | Paste<br/>                                                                                                                                                                                                                                                                           |
| <span id="APPCOMMAND_PRINT"></span><span id="appcommand_print"></span><dl> <dt>**APPCOMMAND\_PRINT**</dt> <dt>33</dt> </dl>                                                                                         | Print current document.<br/>                                                                                                                                                                                                                                                         |
| <span id="APPCOMMAND_REDO"></span><span id="appcommand_redo"></span><dl> <dt>**APPCOMMAND\_REDO**</dt> <dt>35</dt> </dl>                                                                                            | Redo last action.<br/>                                                                                                                                                                                                                                                               |
| <span id="APPCOMMAND_REPLY_TO_MAIL"></span><span id="appcommand_reply_to_mail"></span><dl> <dt>**APPCOMMAND\_REPLY\_TO\_MAIL**</dt> <dt>39</dt> </dl>                                                               | Reply to a mail message.<br/>                                                                                                                                                                                                                                                        |
| <span id="APPCOMMAND_SAVE"></span><span id="appcommand_save"></span><dl> <dt>**APPCOMMAND\_SAVE**</dt> <dt>32</dt> </dl>                                                                                            | Save current document.<br/>                                                                                                                                                                                                                                                          |
| <span id="APPCOMMAND_SEND_MAIL"></span><span id="appcommand_send_mail"></span><dl> <dt>**APPCOMMAND\_SEND\_MAIL**</dt> <dt>41</dt> </dl>                                                                            | Send a mail message.<br/>                                                                                                                                                                                                                                                            |
| <span id="APPCOMMAND_SPELL_CHECK"></span><span id="appcommand_spell_check"></span><dl> <dt>**APPCOMMAND\_SPELL\_CHECK**</dt> <dt>42</dt> </dl>                                                                      | Initiate a spell check.<br/>                                                                                                                                                                                                                                                         |
| <span id="APPCOMMAND_TREBLE_DOWN"></span><span id="appcommand_treble_down"></span><dl> <dt>**APPCOMMAND\_TREBLE\_DOWN**</dt> <dt>22</dt> </dl>                                                                      | Decrease the treble.<br/>                                                                                                                                                                                                                                                            |
| <span id="APPCOMMAND_TREBLE_UP"></span><span id="appcommand_treble_up"></span><dl> <dt>**APPCOMMAND\_TREBLE\_UP**</dt> <dt>23</dt> </dl>                                                                            | Increase the treble.<br/>                                                                                                                                                                                                                                                            |
| <span id="APPCOMMAND_UNDO"></span><span id="appcommand_undo"></span><dl> <dt>**APPCOMMAND\_UNDO**</dt> <dt>34</dt> </dl>                                                                                            | Undo last action.<br/>                                                                                                                                                                                                                                                               |
| <span id="APPCOMMAND_VOLUME_DOWN"></span><span id="appcommand_volume_down"></span><dl> <dt>**APPCOMMAND\_VOLUME\_DOWN**</dt> <dt>9</dt> </dl>                                                                       | Lower the volume.<br/>                                                                                                                                                                                                                                                               |
| <span id="APPCOMMAND_VOLUME_MUTE"></span><span id="appcommand_volume_mute"></span><dl> <dt>**APPCOMMAND\_VOLUME\_MUTE**</dt> <dt>8</dt> </dl>                                                                       | Mute the volume.<br/>                                                                                                                                                                                                                                                                |
| <span id="APPCOMMAND_VOLUME_UP"></span><span id="appcommand_volume_up"></span><dl> <dt>**APPCOMMAND\_VOLUME\_UP**</dt> <dt>10</dt> </dl>                                                                            | Raise the volume.<br/>                                                                                                                                                                                                                                                               |



 

The *uDevice* component indicates the input device that generated the input event, and can be one of the following values.



| Value                                                                                                                                                                                                                                 | Meaning                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| <span id="FAPPCOMMAND_KEY"></span><span id="fappcommand_key"></span><dl> <dt>**FAPPCOMMAND\_KEY**</dt> <dt>0</dt> </dl>            | User pressed a key.<br/>                                                                           |
| <span id="FAPPCOMMAND_MOUSE"></span><span id="fappcommand_mouse"></span><dl> <dt>**FAPPCOMMAND\_MOUSE**</dt> <dt>0x8000</dt> </dl> | User clicked a mouse button.<br/>                                                                  |
| <span id="FAPPCOMMAND_OEM"></span><span id="fappcommand_oem"></span><dl> <dt>**FAPPCOMMAND\_OEM**</dt> <dt>0x1000</dt> </dl>       | An unidentified hardware source generated the event. It could be a mouse or a keyboard event.<br/> |



 

The *dwKeys* component indicates whether various virtual keys are down, and can be one or more of the following values.



| Value                                                                                                                                                                                                               | Meaning                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| <span id="MK_CONTROL"></span><span id="mk_control"></span><dl> <dt>**MK\_CONTROL**</dt> <dt>0x0008</dt> </dl>    | The CTRL key is down.<br/>            |
| <span id="MK_LBUTTON"></span><span id="mk_lbutton"></span><dl> <dt>**MK\_LBUTTON**</dt> <dt>0x0001</dt> </dl>    | The left mouse button is down.<br/>   |
| <span id="MK_MBUTTON"></span><span id="mk_mbutton"></span><dl> <dt>**MK\_MBUTTON**</dt> <dt>0x0010</dt> </dl>    | The middle mouse button is down.<br/> |
| <span id="MK_RBUTTON"></span><span id="mk_rbutton"></span><dl> <dt>**MK\_RBUTTON**</dt> <dt>0x0002</dt> </dl>    | The right mouse button is down.<br/>  |
| <span id="MK_SHIFT"></span><span id="mk_shift"></span><dl> <dt>**MK\_SHIFT**</dt> <dt>0x0004</dt> </dl>          | The SHIFT key is down.<br/>           |
| <span id="MK_XBUTTON1"></span><span id="mk_xbutton1"></span><dl> <dt>**MK\_XBUTTON1**</dt> <dt>0x0020</dt> </dl> | The first X button is down.<br/>      |
| <span id="MK_XBUTTON2"></span><span id="mk_xbutton2"></span><dl> <dt>**MK\_XBUTTON2**</dt> <dt>0x0040</dt> </dl> | The second X button is down.<br/>     |



 

</dd> </dl>

## Return value

If an application processes this message, it should return **TRUE**. For more information about processing the return value, see the Remarks section.

## Remarks

[**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) generates the **WM\_APPCOMMAND** message when it processes the [**WM\_XBUTTONUP**](wm-xbuttonup.md) or [**WM\_NCXBUTTONUP**](wm-ncxbuttonup.md) message, or when the user types an application command key.

If a child window does not process this message and instead calls [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca), **DefWindowProc** will send the message to its parent window. If a top level window does not process this message and instead calls **DefWindowProc**, **DefWindowProc** will call a shell hook with the hook code equal to **HSHELL\_APPCOMMAND**.

To get the coordinates of the cursor if the message was generated by a mouse click, the application can call [**GetMessagePos**](/windows/desktop/api/winuser/nf-winuser-getmessagepos). An application can test whether the message was generated by the mouse by checking whether *lParam* contains **FAPPCOMMAND\_MOUSE**.

Unlike other windows messages, an application should return **TRUE** from this message if it processes it. Doing so will allow software that simulates this message on Windows systems earlier than Windows 2000 to determine whether the window procedure processed the message or called [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) to process it.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)
</dt> <dt>

[**GET\_APPCOMMAND\_LPARAM**](/windows/win32/api/winuser/nf-winuser-get_appcommand_lparam)
</dt> <dt>

[**GET\_DEVICE\_LPARAM**](/windows/win32/api/winuser/nf-winuser-get_device_lparam)
</dt> <dt>

[**GET\_KEYSTATE\_LPARAM**](/windows/win32/api/winuser/nf-winuser-get_keystate_lparam)
</dt> <dt>

[**ShellProc**](/previous-versions/windows/desktop/legacy/ms644991(v=vs.85))
</dt> <dt>

[**WM\_XBUTTONUP**](wm-xbuttonup.md)
</dt> <dt>

[**WM\_NCXBUTTONUP**](wm-ncxbuttonup.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Mouse Input](mouse-input.md)
</dt> </dl>

 

