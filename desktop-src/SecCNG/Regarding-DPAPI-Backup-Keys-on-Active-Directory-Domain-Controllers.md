#Regarding DPAPI Backup Keys on Active Directory Domain Controllers

In the Active Directory database, there exists a set of objects known as DPAPI Backup Keys. These objects include:

BCKUPKEY_P Secret

BCKUPKEY_PREFERRED Secret

BCKUPKEY_guid1
  
BCKUPKEY_guid2
  
These objects are of the schema class “secret” and they exist in the "CN=System,DC=contoso,DC=com” container in the Domain partition.

Normally, domain users encrypt DPAPI-protected data using keys that are derived from their own passwords. However, if the user forgets their password, or if their password is administratively reset or reset from a different computer, the previously encrypted data can no longer be decrypted using the new keys derived from the user’s new password.

In this event, the data can still be decrypted using the Backup keys stored on the Active Directory domain controllers, and then re-encrypted with the user’s new password-derived key.

This implies that anyone who has the DPAPI Backup keys for a domain will be able to decrypt DPAPI-encrypted data for any domain user, even after the user’s password is changed.

The DPAPI Backup keys on Active Directory Domain Controllers are randomly generated only once, during the initial creation of the domain.

Due to the sensitive nature of these keys, it is imperative that access to these keys be protected and regarded as one of the most highly confidential pieces of information in the entire Active Directory domain. By default, only Domain Administrators may access these keys.

As of the time of this writing, there exists no Microsoft-supported way of changing or rotating these DPAPI Backup keys on the domain controllers. In accordance with the document MS-BKRP, it may be possible for 3rd parties to develop an application or script that creates a new DPAPI Backup key and sets the new key to be the preferred key for the domain, however Microsoft does not support these 3rd party solutions and there currently exists no Microsoft implementation of this procedure.

Should the DPAPI Backup keys for the domain be compromised or stolen by a malicious actor, the recommendation is to build a new domain and migrate users to that new domain. If a malicious actor is able to gain access to the DPAPI Backup keys, that implies they have acquired Domain Admin-level access to the domain and can do anything else they want in the domain. The attacker may also plant any other sort of backdoor they wish in the domain with the level of access that they now have, hence the recommendation to migrate to a new domain.

Common-sense Active Directory administration practices are the defense against this sort of doomsday scenario: e.g., do not give Domain Admin permissions to people you don’t trust, protect Active Directory backups with as much vigilance as you protect the domain controllers themselves, etc.
