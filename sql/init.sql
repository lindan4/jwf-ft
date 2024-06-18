-- DROP TABLE IF EXISTS public.coefficient;

CREATE TABLE IF NOT EXISTS public.coefficient
(
    name text COLLATE pg_catalog."default" NOT NULL,
    value numeric(10,2),
    CONSTRAINT coefficient_pkey PRIMARY KEY (name)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.coefficient
    OWNER to postgres;


insert into public.coefficient(name, value)
values ('distance', 0.5);

insert into public.coefficient(name, value)
values ('weight', 0.5);