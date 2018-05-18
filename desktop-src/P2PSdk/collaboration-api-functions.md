---
Description: Collaboration API Functions
ms.assetid: '00c3c1f1-c36c-469a-a644-0ec60f02d25e'
title: Collaboration API Functions
---

# Collaboration API Functions

The Peer Collaboration Infrastructure supports the following functions.



| Function                                                                                       | Description                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PeerCollabAddContact**](peercollabaddcontact.md)                                           | Adds a contact to the contact list of a peer.                                                                                                                                                   |
| [**PeerCollabAsyncInviteContact**](peercollabasyncinvitecontact.md)                           | Sends an invitation to a trusted peer contact to join the sender's Peer Collaboration activity over a secured connection.                                                                       |
| [**PeerCollabAsyncInviteEndpoint**](peercollabasyncinviteendpoint.md)                         | Sends an invitation to a specified peer endpoint to join the sender's Peer Collaboration activity. The availability of the response to the invitation is updated through an asynchronous event. |
| [**PeerCollabCancelInvitation**](peercollabcancelinvitation.md)                               | Cancels an invitation previously sent by the caller to a contact.                                                                                                                               |
| [**PeerCollabCloseHandle**](peercollabclosehandle.md)                                         | Closes the handle to a Peer Collaboration activity invitation.                                                                                                                                  |
| [**PeerCollabDeleteContact**](peercollabdeletecontact.md)                                     | Deletes a contact from the current peer.                                                                                                                                                        |
| [**PeerCollabDeleteEndpointData**](peercollabdeleteendpointdata.md)                           | Deletes the peer endpoint data on the calling peer node that matches the supplied endpoint data.                                                                                                |
| [**PeerCollabDeleteObject**](peercollabdeleteobject.md)                                       | Deletes a peer object from the calling endpoint.                                                                                                                                                |
| [**PeerCollabEnumApplications**](peercollabenumapplications.md)                               | Returns the handle to an enumeration that contains the capabilities registered to a specific peer's endpoint(s).                                                                                |
| [**PeerCollabEnumApplicationRegistrationInfo**](peercollabenumapplicationregistrationinfo.md) | Obtains the enumeration handle used to retrieve peer application information.                                                                                                                   |
| [**PeerCollabEnumContacts**](peercollabenumcontacts.md)                                       | Returns a handle to an enumerated set that contains all of the peer collaboration network contacts currently available on the calling peer.                                                     |
| [**PeerCollabEnumEndpoints**](peercollabenumendpoints.md)                                     | Returns the handle to an enumeration that contains the endpoints associated with a specific peer contact.                                                                                       |
| [**PeerCollabEnumObjects**](peercollabenumobjects.md)                                         | Returns the handle to an enumeration that contains the peer objects associated with a specific peer's endpoint.                                                                                 |
| [**PeerCollabEnumPeopleNearMe**](peercollabenumpeoplenearme.md)                               | Returns a handle to an enumerated set that contains all of the peer collaboration network "people near me" endpoints currently available on the subnet of the calling peer.                     |
| [**PeerCollabExportContact**](peercollabexportcontact.md)                                     | Exports the contact data associated with a peer name to a contact XML data string buffer.                                                                                                       |
| [**PeerCollabGetAppLaunchInfo**](peercollabgetapplaunchinfo.md)                               | Obtains the peer application launch information, including the contact name, the peer endpoint, and the invitation request.                                                                     |
| [**PeerCollabGetApplicationRegistrationInfo**](peercollabgetapplicationregistrationinfo.md)   | Obtains specific application registration information.                                                                                                                                          |
| [**PeerCollabGetContact**](peercollabgetcontact.md)                                           | Obtains the information for a specific peer contact given the peer name of the contact.                                                                                                         |
| [**PeerCollabGetEndpointName**](peercollabgetendpointname.md)                                 | Retrieves the name of the current endpoint of the calling peer previously set by a call to PeerCollabSetEndpointName.                                                                           |
| [**PeerCollabGetEventData**](peercollabgeteventdata.md)                                       | Obtains the data associated with a Peer Collaboration event raised on the peer.                                                                                                                 |
| [**PeerCollabGetInvitationResponse**](peercollabgetinvitationresponse.md)                     | Obtains the response from peer previously invited to join a Peer Collaboration activity.                                                                                                        |
| [**PeerCollabGetPresenceInfo**](peercollabgetpresenceinfo.md)                                 | Retrieves the presence information for the endpoint associated with a specific contact.                                                                                                         |
| [**PeerCollabGetSigninOptions**](peercollabgetsigninoptions.md)                               | Obtains the peer's current signed-in peer collaboration network presence options.                                                                                                               |
| [**PeerCollabInviteContact**](peercollabinvitecontact.md)                                     | Sends an invitation to join a Peer Collaboration activity to a trusted contact. This call is synchronous and, if successful, obtains a response from the contact.                               |
| [**PeerCollabInviteEndpoint**](peercollabinviteendpoint.md)                                   | Sends an invitation to a specified peer endpoint to join the sender's Peer Collaboration activity. This call is synchronous and, if successful, obtains a response from the peer endpoint.      |
| [**PeerCollabParseContact**](peercollabparsecontact.md)                                       | Parses a Unicode string buffer containing contact XML data into a [**PEER\_CONTACT**](peer-contact.md) data structure.                                                                         |
| [**PeerCollabQueryContactData**](peercollabquerycontactdata.md)                               | Retrieves the contact information for the supplied peer endpoint.                                                                                                                               |
| [**PeerCollabRefreshEndpointData**](peercollabrefreshendpointdata.md)                         | Updates the calling peer node with new endpoint data.                                                                                                                                           |
| [**PeerCollabRegisterApplication**](peercollabregisterapplication.md)                         | Registers an application with the local computer so that it can be launched in a peer collaboration activity.                                                                                   |
| [**PeerCollabRegisterEvent**](peercollabregisterevent.md)                                     | Registers an application with the Peer Collaboration infrastructure to receive callbacks for specific Peer Collaboration events.                                                                |
| [**PeerCollabSetEndpointName**](peercollabsetendpointname.md)                                 | Sets the name of the current endpoint used by the peer application.                                                                                                                             |
| [**PeerCollabSetObject**](peercollabsetobject.md)                                             | Creates or updates a peer data object used in a peer collaboration network.                                                                                                                     |
| [**PeerCollabSetPresenceInfo**](peercollabsetpresenceinfo.md)                                 | Updates the caller's presence information to any contacts watching it.                                                                                                                          |
| [**PeerCollabSignIn**](peercollabsignin.md)                                                   | Signs the peer into a hosted Internet (serverless presence) or subnet ("People Near Me") peer collaboration network presence provider.                                                          |
| [**PeerCollabSignOut**](peercollabsignout.md)                                                 | Signs a peer out of a specific type of peer collaboration network presence provider.                                                                                                            |
| [**PeerCollabShutdown**](peercollabshutdown.md)                                               | Shuts down the Peer Collaboration infrastructure and releases any resources associated with it.                                                                                                 |
| [**PeerCollabStartup**](peercollabstartup.md)                                                 | Initializes the Peer Collaboration infrastructure.                                                                                                                                              |
| [**PeerCollabSubscribeEndpointData**](peercollabsubscribeendpointdata.md)                     | Creates a subscription to an available endpoint.                                                                                                                                                |
| [**PeerCollabUnregisterApplication**](peercollabunregisterapplication.md)                     | Unregisters the specific applications of a peer from the local computer.                                                                                                                        |
| [**PeerCollabUnregisterEvent**](peercollabunregisterevent.md)                                 | Deregisters an application from notification about specific Peer Collaboration events.                                                                                                          |
| [**PeerCollabUnsubscribeEndpointData**](peercollabunsubscribeendpointdata.md)                 | Removes a subscription to an endpoint created with PeerCollabSubscribeEndpointData.                                                                                                             |
| [**PeerCollabUpdateContact**](peercollabupdatecontact.md)                                     | Updates a peer participating in a peer collaboration network with new information on a peer contact.                                                                                            |



 

 

 



