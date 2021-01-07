---
description: Using Mutual Exclusion for ASF Streams
ms.assetid: fdd31eac-1dd6-45f0-90fb-d5a74c85db2e
title: Using Mutual Exclusion for ASF Streams
ms.topic: article
ms.date: 05/31/2018
---

# Using Mutual Exclusion for ASF Streams

ASF content can contain multiple streams that are mutually exclusive. These streams cannot be read concurrently but only one of them is read at a time. For example, the file can contain a set of streams that includes the same content encoded at a different bit rate. The stream that is used is determined by the bandwidth available to the application that streams the content. The ASF Mutual Exclusion Object, which is part of the Header Object, stores information about the group of mutually exclusive streams.

In Media Foundation, the *mutual exclusion* object that exposes the [**IMFASFMutualExclusion**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfmutualexclusion) interface exists for every ASF Mutual Exclusion Object. The profile object holds reference to all mutual exclusion objects.

The mutual exclusion object stores information about the group of mutually exclusive streams as records. A mutual exclusion object can have multiple records that can be used to create complex scenarios. Each record contains one or more streams that cannot coexist with streams in another record, maintained by the mutual exclusion object, depending on the type of mutual exclusion, such as bit rate.

A common example of complex mutual exclusion is a file that contains three audio streams of the same content at various bit rates in each of three languages. Only one of the nine streams should be played at a time, but there are two types by which they are mutually exclusive: language and bit rate.

For this example, the nine streams are assigned the following stream numbers:

<dl> 1 - Language 1, bit rate 1  
2 - Language 1, bit rate 2  
3 - Language 1, bit rate 3  
4 - Language 2, bit rate 1  
5 - Language 2, bit rate 2  
6 - Language 2, bit rate 3  
7 - Language 3, bit rate 1  
8 - Language 3, bit rate 2  
9 - Language 3, bit rate 3  
</dl>

This scenario can be implemented by using the following four mutual exclusion objects:

-   The first mutual exclusion object includes streams 1, 2, and 3, mutually exclusive by bit rate. Each stream has its own record.
-   The second mutual exclusion object includes streams 4, 5, and 6, mutually exclusive by bit rate. Each stream has its own record.
-   The third mutual exclusion object includes 7, 8, and 9, mutually exclusive by bit rate. Each stream has its own record.
-   The fourth mutual exclusion object contains three records, the first including streams 1, 2, and 3; the second including streams 4, 5, and 6; and the third including streams 7, 8, and 9. These records are mutually exclusive by language.

When playing a file created in this way, the streaming application selects the language first because it is less likely to change in the middle of presentation and then selects a bit rate.

## Mutual Exclusion Object Creation and Configuration

The following list summarizes the process of configuring a mutual exclusion object:

1.  Create a mutual exclusion object.
2.  Set the type of mutual exclusion.
3.  Configure the mutual exclusion object by adding records and the associated streams.
4.  Add the mutual exclusion object to the profile.

To create and configure a mutual exclusion object

1.  Call [**IMFASFProfile::CreateMutualExclusion**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfprofile-createmutualexclusion) to create an empty mutual exclusion object.
2.  Call [**IMFASFMutualExclusion::SetType**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmutualexclusion-settype) to set the criterion of the mutually exclusive stream.

    The streams can be mutually exclusive by language, bit rate, presentation, and custom criteria. The type is represented as a GUID. For a list of these constants, see [ASF Mutual Exclusion Type GUIDs](asf-mutual-exclusion-type-guids.md).

3.  Call [**IMFASFMutualExclusion::AddRecord**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmutualexclusion-addrecord) to add a record to the mutual exclusion object.

    This method adds an empty record and assigns it a record index starting with zero.

4.  Call [**IMFASFMutualExclusion::AddStreamForRecord**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmutualexclusion-addstreamforrecord) to add the stream number to the record specified by the record index.

    Each record includes one or more streams. Every stream in a record is mutually exclusive of all streams in every other record. To get the number of streams in a record, call [**IMFASFMutualExclusion::GetStreamsForRecord**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmutualexclusion-getstreamsforrecord) by specifying the record index.

    To remove a stream from the record, call [**IMFASFMutualExclusion::RemoveStreamFromRecord**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmutualexclusion-removestreamfromrecord) and specify the record index and the stream number.

5.  Call [**IMFASFProfile::AddMutualExclusion**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfprofile-addmutualexclusion) to add the configured mutual exclusion object to the profile.

## Enumerating Mutual Exclusion Objects in a Profile

If [**IMFASFProfile::AddMutualExclusion**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfprofile-addmutualexclusion) succeeds, it assigns an index to the specified object, starting at zero.

To enumerate the mutual exclusion objects associated with a profile, call [**IMFASFProfile::GetMutualExclusionCount**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfprofile-getmutualexclusioncount) and loop through the list by calling [**IMFASFProfile::GetMutualExclusion**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfprofile-getmutualexclusion). Mutual exclusion indexes are sequential and range between 0 and one less than the number of streams retrieved by **GetMutualExclusionCount**.

A mutual exclusion object is removed from the profile by calling [**IMFASFProfile::RemoveMutualExclusion**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfprofile-removemutualexclusion). The profile reassigns the mutual exclusion indexes so that they are sequential starting with zero. This overwrites previously stored indexes, which are no longer valid after calling this method. This releases the associated mutual exclusion stream records.

## Removing Records in a Mutual Exclusion Object

To remove a record from a mutual exclusion object, call [**IMFASFMutualExclusion::RemoveRecord**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmutualexclusion-removerecord). If this method succeeds, the mutual exclusion object indexes the remaining records so that they are sequential starting with zero. The application should enumerate the records to ensure the correct index for each record. To do so, call [**IMFASFMutualExclusion::GetRecordCount**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmutualexclusion-getrecordcount) and loop through the records by calling [**IMFASFMutualExclusion::GetStreamsForRecord**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmutualexclusion-getstreamsforrecord).

Removing the record with the highest index has no effect on the other indexes.

## Modifying a Mutual Exclusion Object

To change the configuration of the mutual exclusion object in the profile, the application must replace the existing mutual exclusion object with another object that contains the new settings.

To change the configuration of the mutual exclusion object in the profile

1.  Enumerate the mutual exclusion objects in the profile to get the object that needs to be changed.
2.  Call [**IMFASFMutualExclusion::Clone**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfmutualexclusion-clone) to clone the mutual exclusion object.

3.  Configure the cloned object as required.
4.  Call [**IMFASFProfile::RemoveMutualExclusion**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfprofile-removemutualexclusion) to remove the old mutual exclusion object from the profile.

5.  Call [**IMFASFProfile::AddMutualExclusion**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfprofile-addmutualexclusion) to add the updated mutual exclusion object to the profile.

## Related topics

<dl> <dt>

[ASF Profile](asf-profile.md)
</dt> </dl>

 

 



