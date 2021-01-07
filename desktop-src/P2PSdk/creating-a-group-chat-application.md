---
description: This topic provides relevant code samples for the major steps of developing a chat application with the Peer Grouping API, providing a context for each API call.
ms.assetid: 47bb8606-0b7b-4e71-9d6f-c400d6a82e43
title: Creating a Group Chat Application
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Group Chat Application

This topic provides relevant code samples for the major steps of developing a chat application with the Peer Grouping API, providing a context for each API call. UI behaviors and overall application structure are not included.

> [!Note]  
> The complete Peer Group Chat sample application is provided in the Peer SDK. This topic references functions provided within the sample.

 

## Initializing a Group

The first step when constructing a chat application is to initialize the Peer Grouping Infrastructure by calling [**PeerGroupStartup**](/windows/desktop/api/P2P/nf-p2p-peergroupstartup) with the highest supported version. In this case, **PEER\_GROUP\_VERSION** will be defined in the application header file. The version actually supported by the infrastructure is returned in **peerVersion**.


```C++
    PEER_VERSION_DATA peerVersion;

    hr = PeerGroupStartup(PEER_GROUP_VERSION, &peerVersion);
    if (FAILED(hr))
    {
        return hr;
    }
```



## Creating a Group

A chat application must be able to create a peer group if no group is available to join, or if the application user wants to create a new one. To do this, you must create a [**PEER\_GROUP\_PROPERTIES**](/windows/desktop/api/P2P/ns-p2p-peer_group_properties) structure and populate it with the initial settings for the group, including the classifier for the peer group, the friendly name, the creator's peer name, and the presence lifetime. Once this structure has been populated, you pass it to [**PeerGroupCreate**](/windows/desktop/api/P2P/nf-p2p-peergroupcreate).


```C++
//-----------------------------------------------------------------------------
// Function: CreateGroup
//
// Purpose:  Creates a new group with the friendly name.
//
// Returns:  HRESULT
//
HRESULT CreateGroup(PCWSTR pwzName, PCWSTR pwzIdentity)
{
    HRESULT hr = S_OK;
    PEER_GROUP_PROPERTIES props = {0};

    if (SUCCEEDED(hr))
    {
        if ((NULL == pwzName) || (0 == *pwzName))
        {
            hr = E_INVALIDARG;
            DisplayHrError(L"Please enter a group name.", hr);
        }
    }

    if (SUCCEEDED(hr))
    {
        CleanupGroup( );

        props.dwSize = sizeof(props);
        props.pwzClassifier = L"SampleChatGroup";
        props.pwzFriendlyName = (PWSTR) pwzName;
        props.pwzCreatorPeerName = (PWSTR) pwzIdentity;

        hr = PeerGroupCreate(&props, &g_hGroup);
        if (FAILED(hr))
        {
            DisplayHrError(L"Failed to create a new group.", hr);
        }
    }

    if (SUCCEEDED(hr))
    {
        hr = PrepareToChat( );
    }

    return hr;
}
```



## Issuing Invitations

When issuing an invitation, the GMCs of the invitees must be obtained. These can obtained by calling [**PeerIdentityGetXML**](/windows/desktop/api/P2P/nf-p2p-peeridentitygetxml) on the invitee with their identity name. If successful, the identity information (the XML that contains the base-64 encoded certificate with the RSA public key) is written to an external location (a file, in this sample) where the inviter can obtain it and use it to create an invitation.

At this point, a mechanism for the delivery of the invitation to the invitee must be established. This can be email or another secure method of file exchange. In the sample below, the invitation is written to a file which can then be transferred to the invitee's computer.


```C++
//-----------------------------------------------------------------------------
// Function: SaveIdentityInfo
//
// Purpose:  Saves the information for an identity to a file.
//           Displays a message if there was an error.
//
// Returns:  HRESULT
//
HRESULT SaveIdentityInfo(PCWSTR pwzIdentity, PCWSTR pwzFile)
{
    PWSTR pwzXML = NULL;
    HRESULT hr = PeerIdentityGetXML(pwzIdentity, &pwzXML);

    if (FAILED(hr))
    {
        DisplayHrError(L"Unable to retrieve the XML data for the identity.", hr);
    }
    else
    {
        FILE *fp = NULL;
        errno_t err = 0;

        err = _wfopen_s(&fp, pwzFile, L"wb");
        if (err != 0)
        {
            hr = E_FAIL;
            DisplayHrError(L"Please choose a valid path", hr);
        }
        else
        {
            if (fputws(pwzXML, fp) == WEOF)
            {
                hr = E_FAIL;
                DisplayHrError(L"End of file error.", hr);
            }
            fclose(fp);
        }

        PeerFreeData(pwzXML);
    }

    return hr;
}
```



Invitations, like identities, are also issued externally. In this example, the invitation is written to a file with **fputws** where the invitee can obtain it and use it when it calls [**PeerGroupJoin**](/windows/desktop/api/P2P/nf-p2p-peergroupjoin).


```C++
//-----------------------------------------------------------------------------
// Function: CreateInvitation
//
// Purpose:  Creates an invitation file for an identity.
//           Displays a message if there was an error.
//
// Returns:  HRESULT
//
HRESULT CreateInvitation(PCWSTR wzIdentityInfoPath, PCWSTR wzInvitationPath)
{
    HRESULT hr = S_OK;
    WCHAR wzIdentityInfo[MAX_INVITATION] = {0};
    PWSTR pwzInvitation = NULL;
    errno_t  err  = 0;
    FILE *file = NULL;
        
    err = _wfopen_s(&file, wzIdentityInfoPath, L"rb");
    if (err != 0)
    {
        hr = E_FAIL;
        DisplayHrError(L"Please choose a valid path to the identity information file.", hr);
    }
    else
    {
        fread(wzIdentityInfo, sizeof(WCHAR), MAX_INVITATION, file);
        if (ferror(file))
        {
            hr = E_FAIL;
            DisplayHrError(L"File read error occurred.", hr);
        }
        fclose(file);
    }

    if (SUCCEEDED(hr))
    {
        ULONGLONG ulExpire; // adjust time using this structure
        GetSystemTimeAsFileTime((FILETIME *)&ulExpire);

        // 15days in 100 nanoseconds resolution
        ulExpire += ((ULONGLONG) (60 * 60 * 24 * 15)) * ((ULONGLONG)1000*1000*10);

        hr = PeerGroupCreateInvitation(g_hGroup, wzIdentityInfo, (FILETIME*)&ulExpire, 1, (PEER_ROLE_ID*) &PEER_GROUP_ROLE_MEMBER, &pwzInvitation);
        if (FAILED(hr))
        {
            DisplayHrError(L"Failed to create the invitation.", hr);
        }
    }

    if (SUCCEEDED(hr))
    {
        err = _wfopen_s(&file, wzInvitationPath, L"wb");
        if (err != 0)
        {
            hr = E_FAIL;
            DisplayHrError(L"Please choose a valid path to the invitation file.", hr);
        }
        else
        {
            if (fputws(pwzInvitation, file) == WEOF)
            {
                hr = E_FAIL;
                DisplayHrError(L"End of file error.", hr);
            }
            fclose(file);
        }
    }

    PeerFreeData(pwzInvitation);
    return hr;
}
```



## Joining a Peer Group

If the peer is attempting to join a peer group created by another peer, it will need an invitation from that peer. Invitations are delivered by an external process or application to the invitee and saved to a local file, specified in the sample below as *pwzFileName*. The invitation XML blob is read from the file into **wzInvitation** and passed to [**PeerGroupJoin**](/windows/desktop/api/P2P/nf-p2p-peergroupjoin).


```C++
//-----------------------------------------------------------------------------
// Function: JoinGroup
//
// Purpose:  Uses the invitation to join a group with a specific identity.
//           Displays a message if there was an error.
//
// Returns:  HRESULT
//
HRESULT JoinGroup(PCWSTR pwzIdentity, PCWSTR pwzFileName)
{
    HRESULT hr = S_OK;
    WCHAR wzInvitation[MAX_INVITATION] = {0};
    FILE        *file = NULL;
    errno_t     err;

    err = _wfopen_s(&file, pwzFileName, L"rb");
    if (err !=  0)
    {
        hr = E_FAIL;
        DisplayHrError(L"Error opening group invitation file", hr);
        return hr;
    }
    else
    {
        fread(wzInvitation, sizeof(WCHAR), MAX_INVITATION, file);
        if (ferror(file))
        {
            hr = E_FAIL;
            DisplayHrError(L"File read error occurred.", hr);
        }
        fclose(file);

        hr = PeerGroupJoin(pwzIdentity, wzInvitation, NULL, &g_hGroup);
        if (FAILED(hr))
        {
            DisplayHrError(L"Failed to join group.", hr);
        }
    }

    if (SUCCEEDED(hr))
    {
        hr = PrepareToChat( );
    }

    return hr;
}
```



## Register for Peer Events

Before connecting, you should register for every peer event pertinent to the application. In the example below, you register for the following events:

-   PEER\_GROUP\_EVENT\_RECORD\_CHANGED. Since records will be used to contain public chat messages, the application must be notified every time a new one is added. When this peer event is received, the event data exposes the record with the chat message. Applications should only register for those record types they intend to handle directly.
-   PEER\_GROUP\_EVENT\_MEMBER\_CHANGED. The application must be notified when members join or leave the peer group so the list of participants can be updated accordingly.
-   PEER\_GROUP\_EVENT\_STATUS\_CHANGED. Changes to the peer group status must be conveyed to the application. A peer group member is only considered to be available within the peer group when its status indicates that it is connected to the group, synchronized with the peer group record database, and actively listening to record updates.
-   PEER\_GROUP\_EVENT\_DIRECT\_CONNECTION. Private messages between two members and exchanges of data must be conducted over a direct connection, so the application must be able to handle direct connection requests.
-   PEER\_GROUP\_EVENT\_INCOMING\_DATA. After a direct connection is initiated, this peer event alerts the application that a private message has been received.


```C++
//-----------------------------------------------------------------------------
// Function: RegisterForEvents
//
// Purpose:  Registers the EventCallback function so it will be called for only
//           those events that are specified.
//
// Returns:  HRESULT
//
HRESULT RegisterForEvents(void)
{
    HRESULT hr = S_OK;
    PEER_GROUP_EVENT_REGISTRATION regs[] = {
        { PEER_GROUP_EVENT_RECORD_CHANGED, &RECORD_TYPE_CHAT_MESSAGE },
        { PEER_GROUP_EVENT_MEMBER_CHANGED, 0 },
        { PEER_GROUP_EVENT_STATUS_CHANGED, 0 },
        { PEER_GROUP_EVENT_DIRECT_CONNECTION, &DATA_TYPE_WHISPER_MESSAGE },
        { PEER_GROUP_EVENT_INCOMING_DATA, 0 },
    };

    g_hEvent = CreateEvent(NULL, FALSE, FALSE, NULL);
    if (g_hEvent == NULL)
    {
        hr = HRESULT_FROM_WIN32(GetLastError());
    }
    else
    {
        hr = PeerGroupRegisterEvent(g_hGroup, g_hEvent, celems(regs), regs,  &g_hPeerEvent);
    }

    if (SUCCEEDED(hr))
    {
        if (!RegisterWaitForSingleObject(&g_hWait, g_hEvent, EventCallback, NULL, INFINITE, WT_EXECUTEDEFAULT))
        {
            hr = E_UNEXPECTED;
        }
    }

    return hr;
}
```



## Connecting to a Peer Group

Having either created or joined the group and registered for the appropriate events, it's time to go online and begin an active chat session. To do this, you call [**PeerGroupConnect**](/windows/desktop/api/P2P/nf-p2p-peergroupconnect) and pass in the group handle obtained from [**PeerGroupCreate**](/windows/desktop/api/P2P/nf-p2p-peergroupcreate) or [**PeerGroupJoin**](/windows/desktop/api/P2P/nf-p2p-peergroupjoin). After calling this, chat messages will be received as PEER\_GROUP\_EVENT\_RECORD\_CHANGED events.

## Obtaining a List of Peer Group Members

Obtaining a list of members connected to the peer group is simple: call [**PeerGroupEnumMembers**](/windows/desktop/api/P2P/nf-p2p-peergroupenummembers) to retrieve the list of group members, and then iteratively call [**PeerGetNextItem**](/windows/desktop/api/P2P/nf-p2p-peergetnextitem) until all members are retrieved. You should call [**PeerFreeData**](/windows/desktop/api/P2P/nf-p2p-peerfreedata) after you process each member structure, and you must close the enumeration by calling [**PeerEndEnumeration**](/windows/desktop/api/P2P/nf-p2p-peerendenumeration) when processing is complete.


```C++
//-----------------------------------------------------------------------------
// Function: UpdateParticipantList
//
// Purpose:  Update the list of partipants.
//
// Returns:  nothing
//
void UpdateParticipantList(void)
{
    HRESULT          hr = S_OK;
    HPEERENUM        hPeerEnum = NULL;
    PEER_MEMBER   ** ppMember = NULL;

    ClearParticipantList( );
    if (NULL == g_hGroup)
    {
        return;
    }

    // Retrieve only the members currently present in the group.
    hr = PeerGroupEnumMembers(g_hGroup, PEER_MEMBER_PRESENT, NULL, &hPeerEnum);
    if (SUCCEEDED(hr))
    {
        while (SUCCEEDED(hr))
        {
            ULONG cItem = 1;
            hr = PeerGetNextItem(hPeerEnum, &cItem, (PVOID **) &ppMember);
            if (SUCCEEDED(hr))
            {
                if (0 == cItem)
                {
                    PeerFreeData(ppMember);
                    break;
                }
            }

            if (SUCCEEDED(hr))
            {
                if (0 != ((*ppMember)->dwFlags & PEER_MEMBER_PRESENT))
                {
                    AddParticipantName((*ppMember)->pwzIdentity, (*ppMember)->pCredentialInfo->pwzFriendlyName);
                }
                PeerFreeData(ppMember);
            }
        }

        PeerEndEnumeration(hPeerEnum);
    }
}
```



## Sending a Chat Message

In this example, a chat message is sent by placing it in the **data** field of a [**PEER\_RECORD**](/windows/desktop/api/P2P/ns-p2p-peer_record) structure. The record is added to the peer group records by calling [**PeerGroupAddRecord**](/windows/desktop/api/P2P/nf-p2p-peergroupaddrecord), which will publish it and raise the PEER\_GROUP\_EVENT\_RECORD\_CHANGED event on all peers participating in the peer group.


```C++
//-----------------------------------------------------------------------------
// Function: AddChatRecord
//
// Purpose:  This adds a new chat message record to the group.
//
// Returns:  HRESULT
//
HRESULT AddChatRecord(PCWSTR pwzMessage)
{
    HRESULT     hr = S_OK;
    PEER_RECORD record = {0};
    GUID        idRecord;
    ULONGLONG   ulExpire;
    ULONG cch = (ULONG) wcslen(pwzMessage);

    GetSystemTimeAsFileTime((FILETIME *) &ulExpire);

    // Calculate a 2 minute expiration time in 100 nanosecond resolution
    ulExpire += ((ULONGLONG) 60 * 2) * ((ULONGLONG)1000*1000*10);

    // Set up the record
    record.dwSize = sizeof(record);
    record.data.cbData = (cch+1) * sizeof(WCHAR);
    record.data.pbData = (PBYTE) pwzMessage;
    memcpy(&record.ftExpiration, &ulExpire, sizeof(ulExpire));

    PeerGroupUniversalTimeToPeerTime(g_hGroup, &record.ftExpiration, &record.ftExpiration);

    // Set the record type GUID
    record.type = RECORD_TYPE_CHAT_MESSAGE;

    // Add the record to the database
    hr = PeerGroupAddRecord(g_hGroup, &record, &idRecord);
    if (FAILED(hr))
    {
        DisplayHrError(L"Failed to add a chat record to the group.", hr);
    }

    return hr;
}
```



## Receiving a Chat Message

To receive the chat message, create a callback function for the PEER\_GROUP\_EVENT\_RECORD\_CHANGED event that calls a function similar to one below. The record is obtained by calling [**PeerGroupGetRecord**](/windows/desktop/api/P2P/nf-p2p-peergroupgetrecord) on the event data received by a previous call to [**PeerGroupGetEventData**](/windows/desktop/api/P2P/nf-p2p-peergroupgeteventdata) in the callback function. The chat message is stored in the **data** field of this record.


```C++
//-----------------------------------------------------------------------------
// Function: ProcessRecordChanged
//
// Purpose:  Processes the PEER_GROUP_EVENT_RECORD_CHANGED event.
//
// Returns:  nothing
//
void ProcessRecordChanged(PEER_EVENT_RECORD_CHANGE_DATA * pData)
{
    switch (pData->changeType)
    {
        case PEER_RECORD_ADDED:
            if (IsEqualGUID(&pData->recordType, &RECORD_TYPE_CHAT_MESSAGE))
            {
                PEER_RECORD * pRecord = {0};
                HRESULT hr = PeerGroupGetRecord(g_hGroup, &pData->recordId, &pRecord);
                if (SUCCEEDED(hr))
                {
                    DisplayChatMessage(pRecord->pwzCreatorId, (PCWSTR) pRecord->data.pbData);
                    PeerFreeData(pRecord);
                }
            }
            break;

        case PEER_RECORD_UPDATED:
        case PEER_RECORD_DELETED:
        case PEER_RECORD_EXPIRED:
            break;

        default:
            break;
    }
}
```



 

 



