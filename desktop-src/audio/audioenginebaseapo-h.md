---
Description: 'This section contains reference topics for the Audioenginebaseapo.h header.'
ms.assetid: 'D5FA7293-8849-4DDA-9386-6EA590FFC129'
title: 'Audioenginebaseapo.h'
---

# Audioenginebaseapo.h

This section contains reference topics for the Audioenginebaseapo.h header.

## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>APO_FLAG</strong>](apo-flag.md)<br/></td>
<td>The APO_FLAG enumeration defines constants that are used as flags by an audio processing object (APO).<br/></td>
</tr>
<tr class="even">
<td>[<strong>APO_REG_PROPERTIES</strong>](apo-reg-properties.md)<br/></td>
<td>The APO_REG_PROPERTIES structure is used by [<strong>IAudioProcessingObject::GetRegistrationProperties</strong>](iaudioprocessingobject-getregistrationproperties.md) for returning the registration properties of an audio processing object (APO).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>APOInitBaseStruct</strong>](apoinitbasestruct.md)<br/></td>
<td>The APOInitBaseStruct structure is the base initialization header that must precede other initialization data in [<strong>IAudioProcessingObject::Initialize</strong>](iaudioprocessingobject-initialize.md). <br/></td>
</tr>
<tr class="even">
<td>[<strong>APOInitSystemEffects</strong>](apoinitsystemeffects.md)<br/></td>
<td>The APOInitSystemEffects structure gets passed to the system effects APO for initialization.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>APOInitSystemEffects2</strong>](apoinitsystemeffects2.md)<br/></td>
<td>The APOInitSystemEffects2 structure was introduced with Windows 8.1, to make it possible to provide additional initialization context to the audio processing object (APO) for initialization.<br/></td>
</tr>
<tr class="even">
<td>[<strong>AudioFXExtensionParams</strong>](audiofxextensionparams.md)<br/></td>
<td>The AudioFXExtensionParams structure is passed to the system effects ControlPanel Extension PropertyPage via [IShellPropSheetExt::AddPages](http://msdn.microsoft.com/en-us/library/windows/hardware/bb416595.aspx).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAudioProcessingObject</strong>](iaudioprocessingobject.md)<br/></td>
<td>System Effects Audio Processing Objects (sAPOs) are typically used in or called from real-time process threads. However, it is sometimes necessary to use an sAPO in a non real-time mode. For example, when an sAPO is initialized, it is called from a non real-time thread. But when audio processing begins, the sAPO is called from a real-time thread. The <code>IAudioProcessingObject</code> interface exposes methods that enable a client to access the non real-time compliant parts of an sAPO.<br/> The <code>IAudioProcessingObject</code> interface supports the following methods:<br/> <dl>[<strong>IAudioProcessingObject::GetInputChannelCount</strong>](iaudioprocessingobject-getinputchannelcount.md) <br/><br />
[<strong>IAudioProcessingObject::GetLatency</strong>](iaudioprocessingobject-getlatency.md) <br/><br />
[<strong>IAudioProcessingObject::GetRegistrationProperties</strong>](iaudioprocessingobject-getregistrationproperties.md) <br/><br />
[<strong>IAudioProcessingObject::Initialize</strong>](iaudioprocessingobject-initialize.md) <br/><br />
[<strong>IAudioProcessingObject::IsInputFormatSupported</strong>](iaudioprocessingobject-isinputformatsupported.md) <br/><br />
[<strong>IAudioProcessingObject::IsOutputFormatSupported</strong>](iaudioprocessingobject-isoutputformatsupported.md) <br/><br />
[<strong>IAudioProcessingObject::Reset</strong>](iaudioprocessingobject-reset.md) <br/><br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>IAudioProcessingObjectConfiguration</strong>](iaudioprocessingobjectconfiguration.md)<br/></td>
<td>The <code>IAudioProcessingObjectConfiguration</code> interface is used to configure the APO. This interface uses its methods to lock and unlock the APO for processing.<br/> The <code>IAudioProcessingObjectConfiguration</code> interface supports the following methods:<br/> <dl>[<strong>IAudioProcessingObjectConfiguration::LockForProcess</strong>](iaudioprocessingobjectconfiguration-lockforprocess.md) <br/><br />
[<strong>IAudioProcessingObjectConfiguration::UnlockForProcess</strong>](iaudioprocessingobjectconfiguration-unlockforprocess.md) <br/><br />
</dl></td>
</tr>
<tr class="odd">
<td>[<strong>IAudioProcessingObjectRT</strong>](iaudioprocessingobjectrt.md)<br/></td>
<td>This interface can operate in real-time mode and its methods can be called form real-time processing threads. The implementation of the methods for this interface must not block or touch paged memory. Additionally, you must not call any blocking system routines in the implementation of the methods.<br/> The <code>IAudioProcessingObjectRT</code> interface includes the following methods:<br/> <dl>[<strong>IAudioProcessingObjectRT::APOProcess</strong>](iaudioprocessingobjectrt-apoprocess.md) <br/><br />
[<strong>IAudioProcessingObjectRT::CalcInputFrames</strong>](iaudioprocessingobjectrt-calcinputframes.md) <br/><br />
[<strong>IAudioProcessingObjectRT::CalcOutputFrames</strong>](iaudioprocessingobjectrt-calcoutputframes.md) <br/><br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>IAudioSystemEffectsCustomFormats</strong>](iaudiosystemeffectscustomformats.md)<br/></td>
<td>The <code>IAudioSystemEffectsCustomFormats</code> interface is supported in Windows Vista and later versions of Windows. When you develop an audio processing object (APO) to drive an audio adapter with an atypical format, the APO must support the <code>IAudioSystemEffectsCustomFormats</code> interface.<br/> The Windows operating system can instantiate your APO outside the audio engine and use the <code>IAudioSystemEffectsCustomFormats</code> interface to retrieve information about the atypical format. The associated user interface displays the data that is retrieved.<br/>
<blockquote>
[!Important]<br />
Although the <code>IAudioSystemEffectsCustomFormats</code> interface continues to be supported in Windows, note that the type of APO to which you can apply this interface depends on the version of Windows you are targeting. The following table provides more information:
</blockquote>
<br/> 
<table>
<thead>
<tr class="header">
<th>Target OS</th>
<th>Target APO type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Windows Vista</td>
<td>Global effects (GFX)</td>
</tr>
<tr class="even">
<td>Windows 7</td>
<td>Global effects (GFX)</td>
</tr>
<tr class="odd">
<td>Windows 8</td>
<td>Global effects (GFX)</td>
</tr>
<tr class="even">
<td>Windows 8.1</td>
<td>Endpoint effects (EFX)</td>
</tr>
</tbody>
</table>

<p> </p>
<p>The <code>IAudioSystemEffectsCustomFormats</code> interface inherits from <strong>IUnknown</strong> and also supports the following methods:</p>
<dl>[<strong>IAudioSystemEffectsCustomFormats::GetFormat</strong>](iaudiosystemeffectscustomformats-getformat.md)<br />
[<strong>IAudioSystemEffectsCustomFormats::GetFormatCount</strong>](iaudiosystemeffectscustomformats-getformatcount.md)<br />
[<strong>IAudioSystemEffectsCustomFormats::GetFormatRepresentation</strong>](iaudiosystemeffectscustomformats-getformatrepresentation.md)<br />
</dl></td>
</tr>
</tbody>
</table>



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Baudio\audio%5D:%20Audioenginebaseapo.h%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




