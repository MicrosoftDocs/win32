---
Description: This section contains reference topics for the Audioenginebaseapo.h header.
ms.assetid: D5FA7293-8849-4DDA-9386-6EA590FFC129
title: Audioenginebaseapo.h
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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
<td>[<strong>APO_FLAG</strong>](/windows/desktop/api/audioenginebaseapo/ne-audioenginebaseapo-apo_flag)<br/></td>
<td>The APO_FLAG enumeration defines constants that are used as flags by an audio processing object (APO).<br/></td>
</tr>
<tr class="even">
<td>[<strong>APO_REG_PROPERTIES</strong>](/windows/desktop/api/audioenginebaseapo/ns-audioenginebaseapo-apo_reg_properties)<br/></td>
<td>The APO_REG_PROPERTIES structure is used by [<strong>IAudioProcessingObject::GetRegistrationProperties</strong>](/windows/desktop/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobject-getregistrationproperties) for returning the registration properties of an audio processing object (APO).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>APOInitBaseStruct</strong>](/windows/desktop/api/Audioenginebaseapo/ns-audioenginebaseapo-apoinitbasestruct)<br/></td>
<td>The APOInitBaseStruct structure is the base initialization header that must precede other initialization data in [<strong>IAudioProcessingObject::Initialize</strong>](/windows/desktop/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobject-initialize). <br/></td>
</tr>
<tr class="even">
<td>[<strong>APOInitSystemEffects</strong>](/windows/desktop/api/Audioenginebaseapo/ns-audioenginebaseapo-apoinitsystemeffects)<br/></td>
<td>The APOInitSystemEffects structure gets passed to the system effects APO for initialization.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>APOInitSystemEffects2</strong>](/windows/desktop/api/Audioenginebaseapo/ns-audioenginebaseapo-apoinitsystemeffects2)<br/></td>
<td>The APOInitSystemEffects2 structure was introduced with Windows 8.1, to make it possible to provide additional initialization context to the audio processing object (APO) for initialization.<br/></td>
</tr>
<tr class="even">
<td>[<strong>AudioFXExtensionParams</strong>](/windows/desktop/api/Audioenginebaseapo/ns-audioenginebaseapo-__midl___midl_itf_audioenginebaseapo_0000_0007_0001)<br/></td>
<td>The AudioFXExtensionParams structure is passed to the system effects ControlPanel Extension PropertyPage via [IShellPropSheetExt::AddPages](http://msdn.microsoft.com/en-us/library/windows/hardware/bb416595.aspx).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IAudioProcessingObject</strong>](/windows/desktop/api/audioenginebaseapo/nn-audioenginebaseapo-iaudioprocessingobject)<br/></td>
<td>System Effects Audio Processing Objects (sAPOs) are typically used in or called from real-time process threads. However, it is sometimes necessary to use an sAPO in a non real-time mode. For example, when an sAPO is initialized, it is called from a non real-time thread. But when audio processing begins, the sAPO is called from a real-time thread. The <code>IAudioProcessingObject</code> interface exposes methods that enable a client to access the non real-time compliant parts of an sAPO.<br/> The <code>IAudioProcessingObject</code> interface supports the following methods:<br/> <dl>[<strong>IAudioProcessingObject::GetInputChannelCount</strong>](/windows/desktop/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobject-getinputchannelcount) <br/><br />
[<strong>IAudioProcessingObject::GetLatency</strong>](/windows/desktop/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobject-getlatency) <br/><br />
[<strong>IAudioProcessingObject::GetRegistrationProperties</strong>](/windows/desktop/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobject-getregistrationproperties) <br/><br />
[<strong>IAudioProcessingObject::Initialize</strong>](/windows/desktop/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobject-initialize) <br/><br />
[<strong>IAudioProcessingObject::IsInputFormatSupported</strong>](/windows/desktop/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobject-isinputformatsupported) <br/><br />
[<strong>IAudioProcessingObject::IsOutputFormatSupported</strong>](/windows/desktop/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobject-isoutputformatsupported) <br/><br />
[<strong>IAudioProcessingObject::Reset</strong>](/windows/desktop/api/Audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobject-reset) <br/><br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>IAudioProcessingObjectConfiguration</strong>](/windows/desktop/api/audioenginebaseapo/nn-audioenginebaseapo-iaudioprocessingobjectconfiguration)<br/></td>
<td>The <code>IAudioProcessingObjectConfiguration</code> interface is used to configure the APO. This interface uses its methods to lock and unlock the APO for processing.<br/> The <code>IAudioProcessingObjectConfiguration</code> interface supports the following methods:<br/> <dl>[<strong>IAudioProcessingObjectConfiguration::LockForProcess</strong>](/windows/desktop/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobjectconfiguration-lockforprocess) <br/><br />
[<strong>IAudioProcessingObjectConfiguration::UnlockForProcess</strong>](/windows/desktop/api/Audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobjectconfiguration-unlockforprocess) <br/><br />
</dl></td>
</tr>
<tr class="odd">
<td>[<strong>IAudioProcessingObjectRT</strong>](/windows/desktop/api/audioenginebaseapo/nn-audioenginebaseapo-iaudioprocessingobjectrt)<br/></td>
<td>This interface can operate in real-time mode and its methods can be called form real-time processing threads. The implementation of the methods for this interface must not block or touch paged memory. Additionally, you must not call any blocking system routines in the implementation of the methods.<br/> The <code>IAudioProcessingObjectRT</code> interface includes the following methods:<br/> <dl>[<strong>IAudioProcessingObjectRT::APOProcess</strong>](/windows/desktop/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobjectrt-apoprocess) <br/><br />
[<strong>IAudioProcessingObjectRT::CalcInputFrames</strong>](/windows/desktop/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobjectrt-calcinputframes) <br/><br />
[<strong>IAudioProcessingObjectRT::CalcOutputFrames</strong>](/windows/desktop/api/audioenginebaseapo/nf-audioenginebaseapo-iaudioprocessingobjectrt-calcoutputframes) <br/><br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>IAudioSystemEffectsCustomFormats</strong>](/windows/desktop/api/audioenginebaseapo/nn-audioenginebaseapo-iaudiosystemeffectscustomformats)<br/></td>
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
<dl>[<strong>IAudioSystemEffectsCustomFormats::GetFormat</strong>](/windows/desktop/api/audioenginebaseapo/nf-audioenginebaseapo-iaudiosystemeffectscustomformats-getformat)<br />
[<strong>IAudioSystemEffectsCustomFormats::GetFormatCount</strong>](/windows/desktop/api/audioenginebaseapo/nf-audioenginebaseapo-iaudiosystemeffectscustomformats-getformatcount)<br />
[<strong>IAudioSystemEffectsCustomFormats::GetFormatRepresentation</strong>](/windows/desktop/api/audioenginebaseapo/nf-audioenginebaseapo-iaudiosystemeffectscustomformats-getformatrepresentation)<br />
</dl></td>
</tr>
</tbody>
</table>



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Baudio\audio%5D:%20Audioenginebaseapo.h%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




