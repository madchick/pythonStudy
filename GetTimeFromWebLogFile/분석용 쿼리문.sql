delete result_setupxml where substring(col003,1,12)='211.241.227.'
select top 10 * from result_setupxml
select count(*) from result_setupxml
select col001, count(distinct col003) from result_setupxml group by col001 order by col001    /* ��¥�� TM ����� */
select col001, count(*) from result_setupxml group by col001 order by col001                  /* ��¥�� TM ����Ƚ�� */
select col002, count(*) from result_setupxml group by col002 order by col002                  /* �ð��뺰 TM ����Ƚ�� */
select col003, count(*) icount from result_setupxml group by col003 order by icount desc      /* ����ں� TM ����Ƚ�� */

delete result_tmcomsetupxml where substring(col003,1,12)='211.241.227.'
select top 10 * from result_tmcomsetupxml
select count(*) from result_tmcomsetupxml
select col001, count(distinct col003) from result_tmcomsetupxml group by col001 order by col001    /* ��¥�� ����� ����� */
select col001, count(*) from result_tmcomsetupxml group by col001 order by col001                  /* ��¥�� ����� ����Ƚ�� */
select col002, count(*) from result_tmcomsetupxml group by col002 order by col002                  /* �ð��뺰 ����� ����Ƚ�� */
select col003, count(*) icount from result_tmcomsetupxml group by col003 order by icount desc      /* ����ں� ����� ����Ƚ�� */