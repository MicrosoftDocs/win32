---
title: Attribute List
description: Attribute List
ms.assetid: 81fc356e-ee7a-4630-841f-6c1543e022d3
keywords:
- Windows Media Format SDK,attributes
- Advanced Systems Format (ASF),attributes
- ASF (Advanced Systems Format),attributes
- attributes,list of
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Attribute List

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The predefined attributes included with this SDK are presented alphabetically in the following table. Each attribute has a name, a global identifier, and a data type as defined by the appropriate member of the [**WMT\_ATTR\_DATATYPE**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_attr_datatype) enumeration. Some attributes do not use a simple data type, or are formatted according to a structure. Entries for these attributes list a structure name in the data-type column with the data type used to set the value in parentheses.

> [!Note]  
> See [DRM Attribute List](drm-attribute-list.md) for a table of all the DRM-related attributes.

 

When you are programming with these attributes, you should use the global identifier rather than using the name as a string literal. By using the global identifier, any typographical errors will result in an error at compile time.



| Attribute name                                                                       | Global identifier                             | Data type                                            |
|--------------------------------------------------------------------------------------|-----------------------------------------------|------------------------------------------------------|
| [**ASFLeakyBucketPairs**](asfleakybucketpairs.md)                                   | g\_wszASFLeakyBucketPairs                     | **WMT\_TYPE\_BINARY**                                |
| [**AspectRatioX**](aspectratiox.md)                                                 | g\_wszWMAspectRatioX                          | **WMT\_TYPE\_DWORD**                                 |
| [**AspectRatioY**](aspectratioy.md)                                                 | g\_wszWMAspectRatioY                          | **WMT\_TYPE\_DWORD**                                 |
| [**Author**](author.md)                                                             | g\_wszWMAuthor                                | **WMT\_TYPE\_STRING**                                |
| [**AverageLevel**](averagelevel.md)                                                 | g\_wszAverageLevel                            | **WMT\_TYPE\_DWORD**                                 |
| [**BannerImageData**](bannerimagedata.md)                                           | g\_wszWMBannerImageData                       | **WMT\_TYPE\_BINARY**                                |
| [**BannerImageType**](bannerimagetype.md)                                           | g\_wszWMBannerImageType                       | **WMT\_TYPE\_DWORD**                                 |
| [**BannerImageURL**](bannerimageurl.md)                                             | g\_wszWMBannerImageURL                        | **WMT\_TYPE\_STRING**                                |
| [**Bitrate**](bit-rate.md)                                                          | g\_wszWMBitrate                               | **WMT\_TYPE\_DWORD**                                 |
| [**Broadcast**](broadcast.md)                                                       | g\_wszWMBroadcast                             | **WMT\_TYPE\_BOOL**                                  |
| [**BufferAverage**](bufferaverage.md)                                               | g\_wszBufferAverage                           | **WMT\_TYPE\_DWORD**                                 |
| [**Can\_Skip\_Backward**](can-skip-backward.md)                                     | g\_wszWMSkipBackward                          | **WMT\_TYPE\_BOOL**                                  |
| [**Can\_Skip\_Forward**](can-skip-forward.md)                                       | g\_wszWMSkipForward                           | **WMT\_TYPE\_BOOL**                                  |
| [**Copyright**](copyright.md)                                                       | g\_wszWMCopyright                             | **WMT\_TYPE\_STRING**                                |
| [**CopyrightURL**](copyrighturl.md)                                                 | g\_wszWMCopyrightURL                          | **WMT\_TYPE\_STRING**                                |
| [**CurrentBitrate**](currentbitrate.md)                                             | g\_wszWMCurrentBitrate                        | **WMT\_TYPE\_DWORD**                                 |
| [**Description**](description.md)                                                   | g\_wszWMDescription                           | **WMT\_TYPE\_STRING**                                |
| [**DRM\_ContentID**](drm-contentid.md)                                              | g\_wszWMDRM\_ContentID                        | **WMT\_TYPE\_STRING**                                |
| [**DRM\_DRMHeader\_ContentDistributor**](drm-drmheader-contentdistributor.md)       | g\_wszWMDRM\_DRMHeader\_ContentDistributor    | **WMT\_TYPE\_STRING**                                |
| [**DRM\_DRMHeader\_ContentID**](drm-drmheader-contentid.md)                         | g\_wszWMDRM\_DRMHeader\_ContentID             | **WMT\_TYPE\_STRING**                                |
| [**DRM\_DRMHeader\_IndividualizedVersion**](drm-drmheader-individualizedversion.md) | g\_wszWMDRM\_DRMHeader\_IndividualizedVersion | **WMT\_TYPE\_STRING**                                |
| [**DRM\_DRMHeader\_KeyID**](drm-drmheader-keyid.md)                                 | g\_wszWMDRM\_DRMHeader\_KeyID                 | **WMT\_TYPE\_STRING**                                |
| [**DRM\_DRMHeader\_LicenseAcqURL**](drm-drmheader-licenseacqurl.md)                 | g\_wszWMDRM\_DRMHeader\_LicenseAcqURL         | **WMT\_TYPE\_STRING**                                |
| [**DRM\_DRMHeader\_SubscriptionContentID**](drm-drmheader-subscriptioncontentid.md) | g\_wszWMDRM\_DRMHeader\_SubscriptionContentID | **WMT\_TYPE\_STRING**                                |
| [**DRM\_DRMHeader**](drm-drmheader.md)                                              | g\_wszWMDRM\_DRMHeader                        | **WMT\_TYPE\_STRING**                                |
| [**DRM\_IndividualizedVersion**](drm-individualizedversion.md)                      | g\_wszWMDRM\_IndividualizedVersion            | **WMT\_TYPE\_STRING**                                |
| [**DRM\_KeyID**](drm-keyid.md)                                                      | g\_wszWMDRM\_KeyID                            | **WMT\_TYPE\_STRING**                                |
| [**DRM\_LASignatureCert**](drm-lasignaturecert.md)                                  | g\_wszWMDRM\_LASignatureCert                  | **WMT\_TYPE\_STRING**                                |
| [**DRM\_LASignatureLicSrvCert**](drm-lasignaturelicsrvcert.md)                      | g\_wszWMDRM\_LASignatureLicSrvCert            | **WMT\_TYPE\_STRING**                                |
| [**DRM\_LASignaturePrivKey**](drm-lasignatureprivkey.md)                            | g\_wszWMDRM\_LASignaturePrivKey               | **WMT\_TYPE\_STRING**                                |
| [**DRM\_LASignatureRootCert**](drm-lasignaturerootcert.md)                          | g\_wszWMDRM\_LASignatureRootCert              | **WMT\_TYPE\_STRING**                                |
| [**DRM\_LicenseAcqURL**](drm-licenseacqurl.md)                                      | g\_wszWMDRM\_LicenseAcqURL                    | **WMT\_TYPE\_STRING**                                |
| [**DRM\_LicenseID**](drm-licenseid.md)                                              | g\_wszWMDRM\_LicenseID                        | **WMT\_TYPE\_STRING**                                |
| [**DRM\_SourceID**](drm-sourceid.md)                                                | g\_wszWMDRM\_SourceID                         | **WMT\_TYPE\_DWORD**                                 |
| [**DRM\_V1LicenseAcqURL**](drm-v1licenseacqurl.md)                                  | g\_wszWMDRM\_V1LicenseAcqURL                  | **WMT\_TYPE\_STRING**                                |
| [**Duration**](duration.md)                                                         | g\_wszWMDuration                              | **WMT\_TYPE\_QWORD**                                 |
| [**FileSize**](filesize.md)                                                         | g\_wszWMFileSize                              | **WMT\_TYPE\_QWORD**                                 |
| [**HasArbitraryDataStream**](hasarbitrarydatastream.md)                             | g\_wszWMHasArbitraryDataStream                | **WMT\_TYPE\_BOOL**                                  |
| [**HasAttachedImages**](hasattachedimages.md)                                       | g\_wszWMHasAttachedImages                     | **WMT\_TYPE\_BOOL**                                  |
| [**HasAudio**](hasaudio.md)                                                         | g\_wszWMHasAudio                              | **WMT\_TYPE\_BOOL**                                  |
| [**HasFileTransferStream**](hasfiletransferstream.md)                               | g\_wszWMHasFileTransferStream                 | **WMT\_TYPE\_BOOL**                                  |
| [**HasImage**](hasimage.md)                                                         | g\_wszWMHasImage                              | **WMT\_TYPE\_BOOL**                                  |
| [**HasScript**](hasscript.md)                                                       | g\_wszWMHasScript                             | **WMT\_TYPE\_BOOL**                                  |
| [**HasVideo**](hasvideo.md)                                                         | g\_wszWMHasVideo                              | **WMT\_TYPE\_BOOL**                                  |
| [**Is\_Protected**](is-protected.md)                                                | g\_wszWMProtected                             | **WMT\_TYPE\_BOOL**                                  |
| [**Is\_Trusted**](is-trusted.md)                                                    | g\_wszWMTrusted                               | **WMT\_TYPE\_BOOL**                                  |
| [**ISAN**](isan.md)                                                                 | g\_wszISAN                                    | **WMT\_TYPE\_STRING**                                |
| [**IsVBR**](isvbr.md)                                                               | g\_wszWMIsVBR                                 | **WMT\_TYPE\_BOOL**                                  |
| [**NSC\_Address**](nsc-address.md)                                                  | g\_wszWMNSCAddress                            | **WMT\_TYPE\_STRING**                                |
| [**NSC\_Description**](nsc-description.md)                                          | g\_wszWMNSCDescription                        | **WMT\_TYPE\_STRING**                                |
| [**NSC\_Email**](nsc-email.md)                                                      | g\_wszWMNSCEmail                              | **WMT\_TYPE\_STRING**                                |
| [**NSC\_Name**](nsc-name.md)                                                        | g\_wszWMNSCName                               | **WMT\_TYPE\_STRING**                                |
| [**NSC\_Phone**](nsc-phone.md)                                                      | g\_wszWMNSCPhone                              | **WMT\_TYPE\_STRING**                                |
| [**NumberOfFrames**](numberofframes.md)                                             | g\_wszWMNumberOfFrames                        | **WMT\_TYPE\_QWORD**                                 |
| [**OptimalBitrate**](optimalbitrate.md)                                             | g\_wszWMOptimalBitrate                        | **WMT\_TYPE\_DWORD**                                 |
| [**PeakValue**](peakvalue.md)                                                       | g\_wszPeakValue                               | **WMT\_TYPE\_DWORD**                                 |
| [**Rating**](rating.md)                                                             | g\_wszWMRating                                | **WMT\_TYPE\_STRING**                                |
| [**Seekable**](seekable.md)                                                         | g\_wszWMSeekable                              | **WMT\_TYPE\_BOOL**                                  |
| [**Signature\_Name**](signature-name.md)                                            | g\_wszWMSignature\_Name                       | **WMT\_TYPE\_STRING**                                |
| [**Stridable**](stridable.md)                                                       | g\_wszWMStridable                             | **WMT\_TYPE\_BOOL**                                  |
| [**Title**](title.md)                                                               | g\_wszWMTitle                                 | **WMT\_TYPE\_STRING**                                |
| [**VBRPeak**](vbrpeak.md)                                                           | g\_wszVBRPeak                                 | **WMT\_TYPE\_DWORD**                                 |
| [**WM/AlbumArtist**](wm-albumartist.md)                                             | g\_wszWMAlbumArtist                           | **WMT\_TYPE\_STRING**                                |
| [**WM/AlbumCoverURL**](wm-albumcoverurl.md)                                         | g\_wszWMAlbumCoverURL                         | **WMT\_TYPE\_STRING**                                |
| [**WM/AlbumTitle**](wm-albumtitle.md)                                               | g\_wszWMAlbumTitle                            | **WMT\_TYPE\_STRING**                                |
| [**WM/ASFPacketCount**](wm-asfpacketcount.md)                                       | g\_wszWMASFPacketCount                        | **WMT\_TYPE\_QWORD**                                 |
| [**WM/ASFSecurityObjectsSize**](wm-asfsecurityobjectssize.md)                       | g\_wszWMASFSecurityObjectsSize                | **WMT\_TYPE\_QWORD**                                 |
| [**WM/AudioFileURL**](wm-audiofileurl.md)                                           | g\_wszWMAudioFileURL                          | **WMT\_TYPE\_STRING**                                |
| [**WM/AudioSourceURL**](wm-audiosourceurl.md)                                       | g\_wszWMAudioSourceURL                        | **WMT\_TYPE\_STRING**                                |
| [**WM/AuthorURL**](wm-authorurl.md)                                                 | g\_wszWMAuthorURL                             | **WMT\_TYPE\_STRING**                                |
| [**WM/BeatsPerMinute**](wm-beatsperminute.md)                                       | g\_wszWMBeatsPerMinute                        | **WMT\_TYPE\_STRING**                                |
| [**WM/Category**](wm-category.md)                                                   | g\_wszWMCategory                              | **WMT\_TYPE\_STRING**                                |
| [**WM/Codec**](wm-codec.md)                                                         | g\_wszWMCodec                                 | **WMT\_TYPE\_STRING**                                |
| [**WM/Composer**](wm-composer.md)                                                   | g\_wszWMComposer                              | **WMT\_TYPE\_STRING**                                |
| [**WM/Conductor**](wm-conductor.md)                                                 | g\_wszWMConductor                             | **WMT\_TYPE\_STRING**                                |
| [**WM/ContainerFormat**](wm-containerformat.md)                                     | g\_wszWMContainerFormat                       | **WMT\_STORAGE\_FORMAT** (**WMT\_TYPE\_BINARY**)     |
| [**WM/ContentDistributor**](wm-contentdistributor.md)                               | g\_wszWMContentDistributor                    | **WMT\_TYPE\_STRING**                                |
| [**WM/ContentGroupDescription**](wm-contentgroupdescription.md)                     | g\_wszWMContentGroupDescription               | **WMT\_TYPE\_STRING**                                |
| [**WM/Director**](wm-director.md)                                                   | g\_wszWMDirector                              | **WMT\_TYPE\_STRING**                                |
| [**WM/DRM**](wm-drm.md)                                                             | g\_wszWMDRM                                   | **WMT\_TYPE\_STRING**                                |
| [**WM/DVDID**](wm-dvdid.md)                                                         | g\_wszWMDVDID                                 | **WMT\_TYPE\_STRING**                                |
| [**WM/EncodedBy**](wm-encodedby.md)                                                 | g\_wszWMEncodedBy                             | **WMT\_TYPE\_STRING**                                |
| [**WM/EncodingSettings**](wm-encodingsettings.md)                                   | g\_wszWMEncodingSettings                      | **WMT\_TYPE\_STRING**                                |
| [**WM/EncodingTime**](wm-encodingtime.md)                                           | g\_wszWMEncodingTime                          | **FILETIME** (**WMT\_TYPE\_QWORD**)                  |
| [**WM/Genre**](wm-genre.md)                                                         | g\_wszWMGenre                                 | **WMT\_TYPE\_STRING**                                |
| [**WM/GenreID**](wm-genreid.md)                                                     | g\_wszWMGenreID                               | **WMT\_TYPE\_STRING**                                |
| [**WM/InitialKey**](wm-initialkey.md)                                               | g\_wszWMInitialKey                            | **WMT\_TYPE\_STRING**                                |
| [**WM/ISRC**](wm-isrc.md)                                                           | g\_wszWMISRC                                  | **WMT\_TYPE\_STRING**                                |
| [**WM/Language**](wm-language.md)                                                   | g\_wszWMLanguage                              | **WMT\_TYPE\_STRING**                                |
| [**WM/Lyrics**](wm-lyrics.md)                                                       | g\_wszWMLyrics                                | **WMT\_TYPE\_STRING**                                |
| [**WM/Lyrics\_Synchronised**](wm-lyrics-synchronised.md)                            | g\_wszWMLyrics\_Synchronised                  | **WM\_SYNCHRONISED\_LYRICS** (**WMT\_TYPE\_BINARY**) |
| [**WM/MCDI**](wm-mcdi.md)                                                           | g\_wszWMMCDI                                  | **WMT\_TYPE\_BINARY**                                |
| [**WM/MediaClassPrimaryID**](wm-mediaprimaryid.md)                                  | g\_wszWMMediaClassPrimaryID                   | **WMT\_TYPE\_GUID**                                  |
| [**WM/MediaClassSecondaryID**](wm-mediasecondaryid.md)                              | g\_wszWMMediaClassSecondaryID                 | **WMT\_TYPE\_GUID**                                  |
| [**WM/MediaCredits**](wm-mediacredits.md)                                           | g\_wszWMMediaCredits                          | **WMT\_TYPE\_STRING**                                |
| [**WM/MediaIsDelay**](wm-mediaisdelay.md)                                           | g\_wszWMMediaIsDelay                          | **WMT\_TYPE\_BOOL**                                  |
| [**WM/MediaIsFinale**](wm-mediaisfinale.md)                                         | g\_wszWMMediaIsFinale                         | **WMT\_TYPE\_BOOL**                                  |
| [**WM/MediaIsLive**](wm-mediaislive.md)                                             | g\_wszWMMediaIsLive                           | **WMT\_TYPE\_BOOL**                                  |
| [**WM/MediaIsPremiere**](wm-mediaispremiere.md)                                     | g\_wszWMMediaIsPremiere                       | **WMT\_TYPE\_BOOL**                                  |
| [**WM/MediaIsRepeat**](wm-mediaisrepeat.md)                                         | g\_wszWMMediaIsRepeat                         | **WMT\_TYPE\_BOOL**                                  |
| [**WM/MediaIsSAP**](wm-mediaissap.md)                                               | g\_wszWMMediaIsSAP                            | **WMT\_TYPE\_BOOL**                                  |
| [**WM/MediaIsStereo**](wm-mediaisstereo.md)                                         | g\_wszWMMediaIsStereo                         | **WMT\_TYPE\_BOOL**                                  |
| [**WM/MediaIsSubtitled**](wm-mediaissubtitled.md)                                   | g\_wszWMMediaIsSubtitled                      | **WMT\_TYPE\_BOOL**                                  |
| [**WM/MediaIsTape**](wm-mediaistape.md)                                             | g\_wszWMMediaIsTape                           | **WMT\_TYPE\_BOOL**                                  |
| [**WM/MediaNetworkAffiliation**](wm-medianetworkaffiliation.md)                     | g\_wszWMMediaNetworkAffiliation               | **WMT\_TYPE\_STRING**                                |
| [**WM/MediaOriginalBroadcastDateTime**](wm-mediaoriginalbroadcastdatetime.md)       | g\_wszWMMediaOriginalBroadcastDateTime        | **WMT\_TYPE\_STRING**                                |
| [**WM/MediaOriginalChannel**](wm-mediaoriginalchannel.md)                           | g\_wszWMMediaOriginalChannel                  | **WMT\_TYPE\_STRING**                                |
| [**WM/MediaStationCallSign**](wm-mediastationcallsign.md)                           | g\_wszWMMediaStationCallSign                  | **WMT\_TYPE\_STRING**                                |
| [**WM/MediaStationName**](wm-mediastationname.md)                                   | g\_wszWMMediaStationName                      | **WMT\_TYPE\_STRING**                                |
| [**WM/ModifiedBy**](wm-modifiedby.md)                                               | g\_wszWMModifiedBy                            | **WMT\_TYPE\_STRING**                                |
| [**WM/Mood**](wm-mood.md)                                                           | g\_wszWMMood                                  | **WMT\_TYPE\_STRING**                                |
| [**WM/OriginalAlbumTitle**](wm-originalalbumtitle.md)                               | g\_wszWMOriginalAlbumTitle                    | **WMT\_TYPE\_STRING**                                |
| [**WM/OriginalArtist**](wm-originalartist.md)                                       | g\_wszWMOriginalArtist                        | **WMT\_TYPE\_STRING**                                |
| [**WM/OriginalFilename**](wm-originalfilename.md)                                   | g\_wszWMOriginalFilename                      | **WMT\_TYPE\_STRING**                                |
| [**WM/OriginalLyricist**](wm-originallyricist.md)                                   | g\_wszWMOriginalLyricist                      | **WMT\_TYPE\_STRING**                                |
| [**WM/OriginalReleaseTime**](wm-originalreleasetime.md)                             | g\_wszWMOriginalReleaseTime                   | **WMT\_TYPE\_STRING**                                |
| [**WM/OriginalReleaseYear**](wm-originalreleaseyear.md)                             | g\_wszWMOriginalReleaseYear                   | **WMT\_TYPE\_STRING**                                |
| [**WM/ParentalRating**](wm-parentalrating.md)                                       | g\_wszWMParentalRating                        | **WMT\_TYPE\_STRING**                                |
| [**WM/ParentalRatingReason**](wm-parentalratingreason.md)                           | g\_wszWMParentalRatingReason                  | **WMT\_TYPE\_STRING**                                |
| [**WM/PartOfSet**](wm-partofset.md)                                                 | g\_wszWMPartOfSet                             | **WMT\_TYPE\_STRING**                                |
| [**WM/PeakBitrate**](wm-peakbitrate.md)                                             | g\_wszWMPeakBitrate                           | **WMT\_TYPE\_DWORD**                                 |
| [**WM/Period**](wm-period.md)                                                       | g\_wszWMPeriod                                | **WMT\_TYPE\_STRING**                                |
| [**WM/Picture**](/windows/desktop/wmformat/wmpicture)                                      | g\_wszWMPicture                               | **WM\_PICTURE** (**WMT\_TYPE\_BINARY**)              |
| [**WM/PlaylistDelay**](wm-playlistdelay.md)                                         | g\_wszWMPlaylistDelay                         | **WMT\_TYPE\_STRING**                                |
| [**WM/Producer**](wm-producer.md)                                                   | g\_wszWMProducer                              | **WMT\_TYPE\_STRING**                                |
| [**WM/PromotionURL**](wm-promotionurl.md)                                           | g\_wszWMPromotionURL                          | **WMT\_TYPE\_STRING**                                |
| [**WM/ProtectionType**](wm-protectiontype.md)                                       | g\_wszWMProtectionType                        | **WMT\_TYPE\_STRING**                                |
| [**WM/Provider**](wm-provider.md)                                                   | g\_wszWMProvider                              | **WMT\_TYPE\_STRING**                                |
| [**WM/ProviderCopyright**](wm-providercopyright.md)                                 | g\_wszWMProviderCopyright                     | **WMT\_TYPE\_STRING**                                |
| [**WM/ProviderRating**](wm-providerrating.md)                                       | g\_wszWMProviderRating                        | **WMT\_TYPE\_STRING**                                |
| [**WM/ProviderStyle**](wm-providerstyle.md)                                         | g\_wszWMProviderStyle                         | **WMT\_TYPE\_STRING**                                |
| [**WM/Publisher**](wm-publisher.md)                                                 | g\_wszWMPublisher                             | **WMT\_TYPE\_STRING**                                |
| [**WM/RadioStationName**](wm-radiostationname.md)                                   | g\_wszWMRadioStationName                      | **WMT\_TYPE\_STRING**                                |
| [**WM/RadioStationOwner**](wm-radiostationowner.md)                                 | g\_wszWMRadioStationOwner                     | **WMT\_TYPE\_STRING**                                |
| [**WM/SharedUserRating**](wm-shareduserrating.md)                                   | g\_wszWMSharedUserRating                      | **WMT\_TYPE\_DWORD**                                 |
| [**WM/StreamTypeInfo**](wm-streamtypeinfo.md)                                       | g\_wszWMStreamTypeInfo                        | **WM\_STREAM\_TYPE\_INFO** (**WMT\_TYPE\_BINARY**)   |
| [**WM/SubscriptionContentID**](wm-subscriptioncontentid.md)                         | g\_wszWMSubscriptionContentID                 | **WMT\_TYPE\_STRING**                                |
| [**WM/SubTitle**](wm-subtitle.md)                                                   | g\_wszWMSubTitle                              | **WMT\_TYPE\_STRING**                                |
| [**WM/SubTitleDescription**](wm-subtitledescription.md)                             | g\_wszWMSubTitleDescription                   | **WMT\_TYPE\_STRING**                                |
| [**WM/Text**](wm-text.md)                                                           | g\_wszWMText                                  | **WM\_USER\_TEXT** (**WMT\_TYPE\_BINARY**)           |
| [**WM/ToolName**](wm-toolname.md)                                                   | g\_wszWMToolName                              | **WMT\_TYPE\_STRING**                                |
| [**WM/ToolVersion**](wm-toolversion.md)                                             | g\_wszWMToolVersion                           | **WMT\_TYPE\_STRING**                                |
| [**WM/Track**](wm-track.md)                                                         | g\_wszWMTrack                                 | **WMT\_TYPE\_STRING**                                |
| [**WM/TrackNumber**](wm-tracknumber.md)                                             | g\_wszWMTrackNumber                           | **WMT\_TYPE\_STRING**                                |
| [**WM/UniqueFileIdentifier**](wm-uniquefileidentifier.md)                           | g\_wszWMUniqueFileIdentifier                  | **WMT\_TYPE\_STRING**                                |
| [**WM/UserWebURL**](wm-userweburl.md)                                               | g\_wszWMUserWebURL                            | **WM\_USER\_WEB\_URL** (**WMT\_TYPE\_BINARY**)       |
| [**WM/VideoClosedCaptioning**](wm-videoclosedcaptioning.md)                         | g\_wszWMVideoClosedCaptioning                 | **WMT\_TYPE\_BOOL**                                  |
| [**WM/VideoFrameRate**](wm-videoframerate.md)                                       | g\_wszWMVideoFrameRate                        | **WMT\_TYPE\_DWORD**                                 |
| [**WM/VideoHeight**](wm-videoheight.md)                                             | g\_wszWMVideoHeight                           | **WMT\_TYPE\_DWORD**                                 |
| [**WM/VideoWidth**](wm-videowidth.md)                                               | g\_wszWMVideoWidth                            | **WMT\_TYPE\_DWORD**                                 |
| [**WM/WMADRCAverageReference**](wm-wmadrcaveragereference.md)                       | g\_wszWMWMADRCAverageReference                | **WMT\_TYPE\_DWORD**                                 |
| [**WM/WMADRCAverageTarget**](wm-wmadrcaveragetarget.md)                             | g\_wszWMWMADRCAverageTarget                   | **WMT\_TYPE\_DWORD**                                 |
| [**WM/WMADRCPeakReference**](wm-wmadrcpeakreference.md)                             | g\_wszWMWMADRCPeakReference                   | **WMT\_TYPE\_DWORD**                                 |
| [**WM/WMADRCPeakTarget**](wm-wmadrcpeaktarget.md)                                   | g\_wszWMWMADRCPeakTarget                      | **WMT\_TYPE\_DWORD**                                 |
| [**WM/WMCollectionGroupID**](wm-wmcollectiongroupid.md)                             | g\_wszWMWMCollectionGroupID                   | **WMT\_TYPE\_GUID**                                  |
| [**WM/WMCollectionID**](wm-wmcollectionid.md)                                       | g\_wszWMWMCollectionID                        | **WMT\_TYPE\_GUID**                                  |
| [**WM/WMContentID**](wm-wmcontentid.md)                                             | g\_wszWMWMContentID                           | **WMT\_TYPE\_GUID**                                  |
| [**WM/WMShadowFileSourceDRMType**](wm-wmshadowfilesourcedrmtype.md)                 | g\_wszWMWMShadowFileSourceDRMType             | **WMT\_TYPE\_STRING**                                |
| [**WM/WMShadowFileSourceFileType**](wm-wmshadowfilesourcefiletype.md)               | g\_wszWMWMShadowFileSourceFileType            | **WMT\_TYPE\_STRING**                                |
| [**WM/Writer**](wm-writer.md)                                                       | g\_wszWMWriter                                | **WMT\_TYPE\_STRING**                                |
| [**WM/Year**](wm-year.md)                                                           | g\_wszWMYear                                  | **WMT\_TYPE\_STRING**                                |



 

## Remarks

The following constants are defined with the attributes. Each one indicates the number of a specific type of attribute. You do not need to use these values for anything in your applications.



| Constant                 | Value |
|--------------------------|-------|
| g\_dwWMSpecialAttributes | 20    |
| g\_dwWMContentAttributes | 5     |
| g\_dwWMNSCAttributes     | 5     |



 

## Related topics

<dl> <dt>

[**Attributes**](attributes.md)
</dt> </dl>

 

 