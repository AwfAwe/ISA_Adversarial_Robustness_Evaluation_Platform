create database isa;

create table isa.aimodel (
    aimodel_id integer primary key auto_increment,
    aimodel_name varchar(128) not null,
    aimodel_model varchar(128),
    foreign key (aimodel_id) references isa.aimodel(aimodel_id) on delete cascade
);

create table isa.image (
    image_id integer primary key auto_increment,
    image_name varchar(128) not null,
    foreign key (image_id) references isa.image(image_id) on delete cascade
);
