delete result_setupxml where substring(col003,1,12)='211.241.227.'
select top 10 * from result_setupxml
select count(*) from result_setupxml
select col001, count(distinct col003) from result_setupxml group by col001 order by col001    /* 날짜별 TM 사용자 */
select col001, count(*) from result_setupxml group by col001 order by col001                  /* 날짜별 TM 실행횟수 */
select col002, count(*) from result_setupxml group by col002 order by col002                  /* 시간대별 TM 실행횟수 */
select col003, count(*) icount from result_setupxml group by col003 order by icount desc      /* 사용자별 TM 실행횟수 */

delete result_tmcomsetupxml where substring(col003,1,12)='211.241.227.'
select top 10 * from result_tmcomsetupxml
select count(*) from result_tmcomsetupxml
select col001, count(distinct col003) from result_tmcomsetupxml group by col001 order by col001    /* 날짜별 웹뷰어 사용자 */
select col001, count(*) from result_tmcomsetupxml group by col001 order by col001                  /* 날짜별 웹뷰어 실행횟수 */
select col002, count(*) from result_tmcomsetupxml group by col002 order by col002                  /* 시간대별 웹뷰어 실행횟수 */
select col003, count(*) icount from result_tmcomsetupxml group by col003 order by icount desc      /* 사용자별 웹뷰어 실행횟수 */