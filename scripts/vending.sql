create table machine
(
    machine_id int auto_increment
        primary key,
    location           varchar(255) not null
);

create table product
(
    product_name varchar(255) not null,
    price        int          not null,
    product_id   int auto_increment
        primary key
);

create table listing
(
    listing_id         int auto_increment
        primary key,
    product_id         int not null,
    machine_id int not null,
    amount           int not null,
    constraint product_id
        foreign key (product_id) references product (product_id),
    constraint machine_id
        foreign key (machine_id) references machine (machine_id)
);