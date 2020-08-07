USE mydb;

SELECT club_member.member_id, first_name, last_name, description, amount, due_date
FROM   club_member, invoice
WHERE  club_member.member_id = invoice.member_id;

SELECT first_name, middle_name, last_name, professional_title, tier.description
FROM club_member, tier
WHERE club_member.tier_code = tier.code
ORDER BY last_name