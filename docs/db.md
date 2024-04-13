```mermaid
---
title: farmers market models
---
classDiagram
    users <|-- user_account
    accounts <|-- user_account

    class user
    user : +uuid user_id
    user : varchar(255) first_name
    user : varchar(255) last_name
    user : varchar(255) email
    user : varchar(2048) photo_url
    user : varchar(255) password
    class account
    account : +uuid account_id
    account : varchar(255) account_name
    account : varchar(255) email
    account : varchar(2048) photo_url
    class users_accounts
    user_account : +uuid account_id
    user_account : +uuid user_id

```