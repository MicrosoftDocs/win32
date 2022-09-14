---
title: Detailed Object Model Comparison
description: Detailed Object Model Comparison
ms.assetid: 8f08e2a6-1944-4814-b3b7-680a3722e1a0
keywords:
- Windows Media Player,object model
- Windows Media Player object model,version differences
- object model,version differences
- Windows Media Player ActiveX control,version differences
- ActiveX control,version differences
- Windows Media Player Mobile ActiveX control,version differences
- Windows Media Player Mobile,object model
- migration guide,version differences
- versions of Windows Media Player,object model
ms.topic: article
ms.date: 05/31/2018
---

# Detailed Object Model Comparison

The following table compares the Windows Media Player 6.4 object model properties with the Windows Media Player 7 or later object model.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Windows Media Player 6.4 property</th>
<th>Windows Media Player 7 or later equivalent</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>Player6</em>.<strong>AllowChangeDisplaySize</strong></td>
<td>The display of Windows Media Player 7 or later automatically resizes to fit the media. You can set the height and width properties in the &lt;OBJECT&gt; tag or in script.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>AllowScan</strong></td>
<td><em>Controls</em>. <strong>fastForward</strong> and <em>Controls</em>.<strong>fastReverse</strong> are automatically enabled for file types that support these methods.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>AnglesAvailable</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>AnimationAtStart</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>AudioStream</strong></td>
<td>Use <em>Controls</em>.<strong>currentAudioLanguageIndex</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>AudioStreamsAvailable</strong></td>
<td>Use <em>Controls</em>.<strong>audioLanguageCount</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>AutoRewind</strong></td>
<td>Use <em>Controls</em>.<strong>currentPosition</strong> in script to specify or retrieve the current position. Alternatively, use markers and the <em>Player</em>.<strong>markerHit</strong> event.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>AutoSize</strong></td>
<td>Automatic sizing is the default behavior. To override automatic sizing, set the height and width properties in the &lt;OBJECT&gt; tag or in script.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>AutoStart</strong></td>
<td>Use <em>Settings</em>.<strong>autoStart</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>Balance</strong></td>
<td>Use <em>Settings</em>.<strong>balance</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>Bandwidth</strong></td>
<td>Use <em>Network</em>.<strong>bandWidth</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>BaseURL</strong></td>
<td>Use <em>Settings</em>.<strong>baseURL</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>BufferingCount</strong></td>
<td>Use <em>Network.</em><strong>bufferingCount</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>BufferingProgress</strong></td>
<td>Use <em>Network</em>.<strong>bufferingProgress</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>BufferingTime</strong></td>
<td>Use <em>Network</em>.<strong>bufferingTime</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>ButtonsAvailable</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>CanPreview</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>CanScan</strong></td>
<td>Use <em>Controls</em>.<strong>isAvailable</strong>(&quot;FastForward&quot;) and <em>Controls</em>.<strong>isAvailable</strong>(&quot;FastReverse&quot;).</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>CanSeek</strong></td>
<td>Use <em>Controls</em>.<strong>isAvailable</strong> to test whether a particular seek method can be performed.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>CanSeekToMarkers</strong></td>
<td>Use <em>Controls</em>.<strong>isAvailable</strong>(&quot;CurrentMarker&quot;). Use <em>Media</em>.<strong>markerCount</strong> to retrieve the count of markers in a particular media item. Use <em>Controls</em>.<strong>currentMarker</strong> to specify or retrieve the current marker number.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>CaptioningID</strong></td>
<td>Use <em>ClosedCaption</em>.<strong>captioningID</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>CCActive</strong></td>
<td>Not available. See <a href="closed-captioning.md">Closed Captioning</a> for information about how closed captioning has changed in Windows Media Player.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>ChannelDescription</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>ChannelName</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>ChannelURL</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>ClickToPlay</strong></td>
<td>Not available. You should provide controls in your user interface to start playback. Alternatively, the user can right-click the video image to open a pop-up menu that contains a <strong>Play/Pause</strong> selection if <em>Player</em>.<strong>enableContextMenu</strong> equals true.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>ClientID</strong></td>
<td>Not available.Windows Media Player 9 Series or later allows the user to select whether a unique Player ID is transmitted to content providers.<br/> If the user selects this option, the Player sends a unique ID to the Windows Media server. The ID is logged in the server's log file, located in the ..<em>system32\logfiles</em> folder by default. The log field name is &quot;c-playerid&quot;. Server logging is not enabled by default in Windows Media Services.<br/> If the user does not select this option, the server generates a random session ID, which is unique for each client for a given session.<br/> For more information, see the Windows Media Services 9 Series documentation.<br/></td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>CodecCount</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>ColorKey</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>ConnectionSpeed</strong></td>
<td>Not available. Use <em>Network</em>.<strong>bitRate</strong> to determine the current bit rate.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>ContactAddress</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>ContactEmail</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>ContactPhone</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>CreationDate</strong></td>
<td>Use <em>MediaCollection</em>.<strong>getMediaAtom</strong>(&quot;CreationDate&quot;) to retrieve the index of the creation date atom. Use <em>Media</em>.<strong>getItemInfoByAtom</strong> to retrieve the metadata.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>CurrentAngle</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>CurrentAudioStream</strong></td>
<td>Use <em>Controls</em>.<strong>currentAudioLanguageIndex</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>CurrentButton</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>CurrentCCService</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>CurrentChapter</strong></td>
<td>Retrieve the current playlist. If the current playlist is not the same one as the playlist returned by <em>Cdrom</em>.<strong>playlist</strong>, then there is no current chapter. Otherwise, the current chapter number is the index of the current media in the current playlist.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>CurrentDiscSide</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>CurrentDomain</strong></td>
<td>Use <em>DVD</em>.<strong>domain</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>CurrentMarker</strong></td>
<td>Use <em>Controls</em>.<strong>currentMarker</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>CurrentPosition</strong></td>
<td>Use <em>Controls</em>.<strong>currentPosition</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>CurrentSubpictureStream</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>CurrentTime</strong></td>
<td>Use <em>Controls</em>.<strong>currentPositionTimeCode</strong>, <em>Controls</em>.<strong>currentPositionString</strong>, or <em>Controls</em>.<strong>currentPosition.</strong></td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>CurrentTitle</strong></td>
<td>Retrieve the current playlist. If the current playlist is the same one as the playlist returned by <em>Cdrom</em>.<strong>playlist</strong>, then the title number is the index of the current media in the current playlist.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>CurrentVolume</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>CursorType</strong></td>
<td>Not available. Use Internet Explorer styles instead.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>DefaultFrame</strong></td>
<td>Use <em>Settings</em>.<strong>defaultFrame</strong>, or use a <PARAM> attribute in the &lt;OBJECT&gt; element:
<pre data-space="preserve"><code>\<PARAM NAME=&quot;defaultFrame&quot; VALUE=&quot;right&quot;></code></pre></td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>DisplayBackColor</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>DisplayForeColor</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>DisplayMode</strong></td>
<td>The current position can be retrieved in seconds from the beginning as a <strong>Number</strong> using <em>Controls</em>.<strong>currentPosition</strong>, as a <strong>String</strong> formatted as HH:MM:SS (hours, minutes, seconds) using <em>Controls</em>.<strong>currentPositionString</strong>, or in time code format using <em>Controls</em>.<strong>currentPositionTimeCode</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>DisplaySize</strong></td>
<td>The default display automatically resizes to fit the media. You can set the height and width properties in the &lt;OBJECT&gt; tag, or in script. Use <em>Player</em>.<strong>fullScreen</strong> to switch to full-screen mode.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>Duration</strong></td>
<td>Use <em>Media</em>.<strong>duration</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>DVD</strong></td>
<td>Use <em>Player</em>.<strong>DVD</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>EnableContextMenu</strong></td>
<td>Use <em>Player</em>.<strong>enableContextMenu</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>Enabled</strong></td>
<td>Use <em>Player</em>.<strong>enabled</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>EnableFullScreenControls</strong></td>
<td>When using Windows Media Player 9 Series or later, full-screen controls are enabled automatically unless <em>Player</em>.<strong>uiMode</strong> = &quot;none&quot;.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>EnablePositionControls</strong></td>
<td>Not available. You can provide custom controls or use <em>Player</em>.<strong>uimode</strong> to choose a default configuration.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>EnableTracker</strong></td>
<td>Not available. You can provide a custom control or use <em>Player</em>.<strong>uimode</strong> to choose a default configuration.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>EntryCount</strong></td>
<td>Use <em>Playlist</em>.<strong>count</strong></td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>ErrorCode</strong></td>
<td>Use <em>ErrorItem</em>.<strong>errorCode</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>ErrorCorrection</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>ErrorDescription</strong></td>
<td>Use <em>ErrorItem</em>.<strong>errorDescription</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>FileName</strong></td>
<td>Use <em>Player</em>.<strong>URL</strong> or <em>Player</em>.<strong>currentMedia</strong>. Use <em>Controls</em>.<strong>currentItem</strong> when working within a playlist.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>FramesPerSecond</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>HasError</strong></td>
<td>Use <em>Error</em>.<strong>errorCount</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>HasMultipleItems</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>ImageSourceHeight</strong></td>
<td>Use <em>Media</em>.<strong>imageSourceHeight</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>ImageSourceWidth</strong></td>
<td>Use <em>Media</em>.<strong>imageSourceWidth</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>InvokeURLs</strong></td>
<td>Use <em>Settings</em>.<strong>invokeURLs</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>IsBroadcast</strong></td>
<td>Use <em>Network</em>.<strong>sourceProtocol</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>IsDurationValid</strong></td>
<td>Not available. <em>Media</em>.<strong>duration</strong> contains a valid value when used with the current media object.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>Language</strong></td>
<td>Use <em>Controls</em>.<strong>currentAudioLanguage</strong></td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>LostPackets</strong></td>
<td>Use <em>Network</em>.<strong>lostPackets</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>MarkerCount</strong></td>
<td>Use <em>Media</em>.<strong>markerCount</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>Mute</strong></td>
<td>Use <em>Settings</em>.<strong>mute</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>OpenState</strong></td>
<td>Use <em>Player</em>.<strong>openState</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>PlayCount</strong></td>
<td>Use <em>Settings</em>.<strong>playCount</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>PlayState</strong></td>
<td>Use <em>Player</em>.<strong>playState</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>PreviewMode</strong></td>
<td>Not available. Use a script loop structure with an HTML timer to duplicate this functionality.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>Rate</strong></td>
<td>Use <em>Settings</em>.<strong>rate</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>ReadyState</strong></td>
<td>Use <em>Player</em>.<strong>openState</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>ReceivedPackets</strong></td>
<td>Use <em>Network</em>.<strong>receivedPackets</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>ReceptionQuality</strong></td>
<td>Use <em>Network</em>.<strong>receptionQuality</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>RecoveredPackets</strong></td>
<td>Use <em>Network</em>.<strong>recoveredPackets</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>Root</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>SAMIFileName</strong></td>
<td>Use <em>ClosedCaption</em>.<strong>SAMIFileName</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>SAMILang</strong></td>
<td>Use <em>ClosedCaption</em>.<strong>SAMILang</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>SAMIStyle</strong></td>
<td>Use <em>ClosedCaption</em>.<strong>SAMIStyle</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>SelectionEnd</strong></td>
<td>Use <em>Media</em>.<strong>duration</strong> to determine the length of a <strong>Media</strong> object. Use a marker with <em>Controls</em>.<strong>currentMarker</strong> to specify a custom end position.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>SelectionStart</strong></td>
<td>Use <em>Controls</em>.<strong>currentPosition</strong> to start playback from a particular position or use a marker with <em>Controls</em>.<strong>currentMarker</strong> to specify a custom start position.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>SendErrorEvents</strong></td>
<td>Errors are queued. Use the <strong>Error</strong> object and the <strong>ErrorItem</strong> object to retrieve error information.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>SendKeyboardEvents</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>SendMouseClickEvents</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>SendMouseMoveEvents</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>SendOpenStateChangeEvents</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>SendPlayStateChangeEvents</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>SendWarningEvents</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>ShowAudioControls</strong></td>
<td>Not available. You can provide custom controls or use <em>Player</em>.<strong>uimode</strong> to choose a default configuration.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>ShowCaptioning</strong></td>
<td>Not available. You can provide a custom closed caption display.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>ShowControls</strong></td>
<td>Not available. You can provide custom controls or use <em>Player</em>.<strong>uimode</strong> to choose a default configuration.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>ShowDisplay</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>ShowGotoBar</strong></td>
<td>Not available. You can provide custom functionality using the Media object</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>ShowPositionControls</strong></td>
<td>Not available. You can provide custom controls or use <em>Player</em>.<strong>uimode</strong> to choose a default configuration.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>ShowStatusBar</strong></td>
<td>Not available. You can provide custom controls or use <em>Player</em>.<strong>uimode</strong> to choose a default configuration.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>ShowTracker</strong></td>
<td>Not available. You can provide custom controls or use <em>Player</em>.<strong>uimode</strong> to choose a default configuration.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>SourceLink</strong></td>
<td>Use <em>Media</em>.<strong>sourceURL</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>SourceProtocol</strong></td>
<td>Use <em>Network</em>.<strong>sourceProtocol</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>StreamCount</strong></td>
<td>Not available. Use <em>Controls</em>.<strong>audioLanguageCount</strong> to retrieve the number of audio language streams.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>SubpictureOn</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>SubpictureStreamsAvailable</strong></td>
<td>Not available</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>TitlesAvailable</strong></td>
<td>Use the following:<code>Player.Cdrom.playlist.count - 1</code><br/></td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>TotalTitleTime</strong></td>
<td>Use <em>currentMedia</em>.<strong>duration</strong> or <em>currentMedia</em>.<strong>durationString</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>TransparentAtStart</strong></td>
<td>Use script to specify the height and width values to make the player visible or invisible.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>UniqueID</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>VideoBorder3D</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>VideoBorderColor</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>VideoBorderWidth</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>Volume</strong></td>
<td>Use <em>Settings</em>.<strong>Volume</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>VolumesAvailable</strong></td>
<td>Not available.</td>
</tr>
</tbody>
</table>



 

The following table compares the Windows Media Player version 6.4 object model methods with the Windows Media Player 7 or later object model.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Windows Media Player 6.4 method</th>
<th>Windows Media Player 7 or later equivalent</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>Player6</em>.<strong>AboutBox</strong></td>
<td>Use <em>Player</em>.<strong>versionInfo</strong> to retrieve the version of Windows Media Player.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>BackwardScan</strong></td>
<td>Use <em>Settings</em>.<strong>rate</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>ButtonActivate</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>ButtonSelectAndActivate</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>Cancel</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>ChapterPlay</strong></td>
<td>If already playing the specified title playlist, retrieve the desired chapter as a media object using the following syntax:
<pre data-space="preserve"><code>var media = Player.currentPlaylist.item(index);</code></pre>
Then, specify <em>Player</em>.<strong>currentMedia</strong> using the media object returned.<br/></td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>ChapterPlayAutoStop</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>ChapterSearch</strong></td>
<td>If already playing the specified title playlist, retrieve the desired chapter as a media object using the following syntax:
<pre data-space="preserve"><code>var media = Player.currentPlaylist.item(index);</code></pre>
Then, specify <em>Player</em>.<strong>currentMedia</strong> using the media object returned.<br/></td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>FastForward</strong></td>
<td>Use <em>Controls</em>.<strong>fastForward</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>FastReverse</strong></td>
<td>Use <em>Controls</em>.<strong>fastReverse</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>ForwardScan</strong></td>
<td>Use <em>Settings</em>.<strong>rate</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>GetAllGPRMs</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>GetAllSPRMs</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>GetAudioLanguage</strong></td>
<td>Use <em>Controls</em>.<strong>currentAudioLanguage</strong> to retrieve the LCID of the current audio language.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>GetCodecDescription</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>GetCodecInstalled</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>GetCodecURL</strong></td>
<td>Use <em>ErrorItem</em>.<strong>customUrl</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>GetCurrentEntry</strong></td>
<td>Use script to loop through the current playlist. Use <em>Media</em>.<strong>isIdentical</strong> to compare each entry in the playlist to the <em>Player</em>.<strong>currentMedia</strong> object.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>GetMarkerName</strong></td>
<td>Use <em>Media</em>.<strong>getMarkerName</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>GetMarkerTime</strong></td>
<td>Use <em>Media</em>.<strong>getMarkerTime</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>GetMediaInfoString</strong></td>
<td>Use <em>Media</em>.<strong>getItemInfo</strong>, <em>Media</em>.<strong>getItemInfoByAtom</strong>, and their associated methods to retrieve metadata.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>GetMediaParameter</strong></td>
<td>Use <em>Playlist</em>.<strong>item</strong> to retrieve a media item. Then use <em>Media</em>.<strong>getItemInfo</strong> to retrieve the parameter string.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>GetMediaParameterName</strong></td>
<td>Use <em>Playlist</em>.<strong>item</strong> to retrieve a media item. Then use <em>Media</em>.<strong>getAttributeName</strong> to retrieve the parameter string.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>GetMoreInfoURL</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>GetNumberOfChapters</strong></td>
<td>If a title is currently playing, use <em>currentPlaylist</em>.<strong>count</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>GetStreamGroup</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>GetStreamName</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>GetStreamSelected</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>GetSubpictureLanguage</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>GoUp</strong></td>
<td>Use <em>DVD</em>.<strong>back</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>IsSoundCardEnabled</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>LeftButtonSelect</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>LowerButtonSelect</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>MenuCall</strong></td>
<td>Use <em>DVD</em>.<strong>titleMenu</strong> or <em>DVD</em>.<strong>topMenu</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>Next</strong></td>
<td>Use <em>Controls</em>.<strong>next</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>NextPGSearch</strong></td>
<td>Use <em>Controls</em>.<strong>next</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>Open</strong></td>
<td>Use <em>Player</em>.<strong>URL</strong> or <em>Player</em>.<strong>currentMedia</strong>. Files always open asynchronously.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>Pause</strong></td>
<td>Use <em>Controls</em>.<strong>pause</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>Play</strong></td>
<td>Use <em>Controls</em>.<strong>play</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>Previous</strong></td>
<td>Use <em>Controls</em>.<strong>previous</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>PrevPGSearch</strong></td>
<td>Use <em>Controls</em>.<strong>previous</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>ResumeFromMenu</strong></td>
<td>Use <em>DVD</em>.<strong>resume</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>RightButtonSelect</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>SetCurrentEntry</strong></td>
<td>Retrieve a media object using <em>currentPlaylist</em>.<strong>item</strong>(<em>entryNumber</em>). Then, specify the retrieved media object using <em>Controls</em>.<strong>currentItem</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>ShowDialog</strong></td>
<td>Not available.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>StillOff</strong></td>
<td>Use <em>Controls</em>.<strong>play</strong>. Alternatively, use <em>Controls</em>.<strong>Next</strong> if currently in still mode.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>Stop</strong></td>
<td>Use <em>Controls</em>.<strong>stop</strong>.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>StreamSelect</strong></td>
<td>Not available. Use <em>Controls</em>.<strong>currentAudioLanguage</strong> to specify an audio language stream.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>TimePlay</strong></td>
<td>From the root playlist, use <em>currentPlaylist</em>.<strong>item</strong>(<em>index</em>) to retrieve a media object. Then, set the media object as the current one using <em>Controls</em>.<strong>currentItem</strong>. Then, specify <em>Controls</em>.<strong>currentPosition</strong> using a time value in seconds.</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>TimeSearch</strong></td>
<td>Use <em>Controls</em>.<strong>currentPosition</strong>.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>TitlePlay</strong></td>
<td>If already playing the specified title playlist, retrieve the desired chapter as a media object using the following syntax:
<pre data-space="preserve"><code>var media = Player.currentPlaylist.item(index);</code></pre>
Then, specify <em>Player</em>.<strong>currentMedia</strong> using the media object returned.<br/> Alternatively, use <em>currentPlaylist</em>.<strong>item</strong> to retrieve a media object, and then use the media object returned to specify <em>Controls</em>.<strong>currentItem</strong>.<br/></td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>TopPGSearch</strong></td>
<td>Not available.</td>
</tr>
<tr class="odd">
<td><em>Player6</em>.<strong>UOPValid</strong></td>
<td>Not available</td>
</tr>
<tr class="even">
<td><em>Player6</em>.<strong>UpperButtonSelect</strong></td>
<td>Not available.</td>
</tr>
</tbody>
</table>



 

The following table compares the Windows Media Player version 6.4 object model events with the Windows Media Player 7 or later object model.



| Windows Media Player 6.4 event  | Windows Media Player 7 or later equivalent                                                                                                                                                                               |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Player6*.**Buffering**         | Use *Player*.**Buffering**.                                                                                                                                                                                              |
| *Player6*.**Click**             | Use *Player*.**Click**                                                                                                                                                                                                   |
| *Player6*.**DblClick**          | Use *Player*.**DoubleClick**                                                                                                                                                                                             |
| *Player6*.**Disconnect**        | Not available.                                                                                                                                                                                                           |
| *Player6*.**DisplayModeChange** | Not available.                                                                                                                                                                                                           |
| *Player6*.**DVDNotify**         | *Player*.**DomainChange** and *Player*.**OpenPlaylistSwitch** are DVD-specific events. Other events related to playlists, media, and CD-ROM media may apply as well depending on the application.                        |
| *Player6*.**EndOfStream**       | Use *Player*.**PlayState**.                                                                                                                                                                                              |
| *Player6*.**Error**             | The event is unchanged. Errors, however, are queued. Use the **Error** object with the **ErrorItem** object to retrieve error information from the queue. See the example code in the preceding section, Error handling. |
| *Player6*.**KeyDown**           | Use *Player*.**Keydown**                                                                                                                                                                                                 |
| *Player6*.**KeyPress**          | Use *Player*.**KeyPress**                                                                                                                                                                                                |
| *Player6*.**KeyUp**             | Use *Player*.**KeyUp**                                                                                                                                                                                                   |
| *Player6*.**MarkerHit**         | Use *Player*.**MarkerHit**.                                                                                                                                                                                              |
| *Player6*.**MouseDown**         | Use *Player*.**MouseDown**                                                                                                                                                                                               |
| *Player6*.**MouseMove**         | Use *Player*.**MouseMove**                                                                                                                                                                                               |
| *Player6*.**MouseUp**           | Use *Player*.**MouseUp**                                                                                                                                                                                                 |
| *Player6*.**NewStream**         | Use *Player*.**OpenStateChange**                                                                                                                                                                                         |
| *Player6*.**OpenStateChange**   | Use *Player*.**OpenStateChange**.                                                                                                                                                                                        |
| *Player6*.**PlayStateChange**   | Use *Player*.**PlayStateChange**.                                                                                                                                                                                        |
| *Player6*.**PositionChange**    | Use *Player*.**PositionChange**.                                                                                                                                                                                         |
| *Player6*.**ReadyStateChange**  | Use *Player*.**PlayStateChange**.                                                                                                                                                                                        |
| *Player6*.**ScriptCommand**     | Use *Player*.**ScriptCommand**.                                                                                                                                                                                          |
| *Player6*.**Warning**           | Not available.                                                                                                                                                                                                           |



 

## Related topics

<dl> <dt>

[**Object Model Migration Guide**](object-model-migration-guide.md)
</dt> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 





