delete result_tmp where substring(col003,1,12)='211.241.227.'
select top 10 * from result_tmp
select count(*) from result_tmp
select col001, count(distinct col003) from result_tmp group by col001 order by col001    /* ��¥�� TM ����� */
select col001, count(*) from result_tmp group by col001 order by col001                  /* ��¥�� TM ����Ƚ�� */
select col002, count(*) from result_tmp group by col002 order by col002                  /* �ð��뺰 TM ����Ƚ�� */
select col003, count(*) icount from result_tmp group by col003 order by icount desc      /* ����ں� TM ����Ƚ�� */



